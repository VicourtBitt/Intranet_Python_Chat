"""This is the main module of this project, it'll only run with the other 3 other
modules, they are the: 'ClearTerminalModule', 'UserCreationModule' and the 'UserLoginModule'.

Created by VicourtBitt, used in PyChat/Intranet Chat Project.
GitHub: https://github.com/VicourtBitt/Intranet_Python_Chat"""

# Built-In Python Modules
from datetime import datetime
import json
import sys
import ast

# Third-Party Python Modules
import paho.mqtt.client as mqtt
from paho.mqtt import publish
import platform

# Self Made Python Modules
from UserCreationModuleNEW import UserCreation # , _publish_update (removed from main, added into module)
from UserLoginModuleNEW import user_login, user_logout
from CleanTerminalModule import clean_terminal
import UserLoginModuleNEW

# MQTT TOPICS - Pay Attention, they are very important
MQTT_LOGIN_DICT = 'login-intranetchat'
MQTT_LOG = 'chat-intranetchat'

# MQTT Variables
MQTT_HOST = 'test.mosquitto.org'
MQTT_PORT = 1883

# Formated variables that will be used
_actual_datetime = datetime.now().strftime('%d/%m - %H:%M')
_command_str = 'Write your message: (Without ACCENTs, to leave write !leave): '
rep = '\\'

# For debugging purposes
interrupt = input("Debug: ")


class OnScreen:
    '''This class has ways to see in which page we are at the moment.'''

    def __init__(self, page_name, page_state= False):
        self.page_name = page_name
        self.page_state = page_state

    def _show_page(self):
        ''' This instance method show us the page we want to see'''
        callabe_pages = {'chats' : _send_message,
                               'log' : _send_log,
                          'logout' : user_logout}
        
        do_with_cpages = callabe_pages.get(self.page_name)
        self.page_state = True
        do_with_cpages()


# Class Objects below
chat_page = OnScreen('chats')
log_page = OnScreen('log')
logout_page = OnScreen('logout')

# Dictionaries and Lists that will be used around the code
_callable_objects = {'log' : log_page,
                  'chats' : chat_page,
               'logout' : logout_page}

_retained_log = []
in_retained_log = bool(_retained_log)
_log = []


def type_debug():
    print("\n")
    for message in _log:
        print(message)
    print(type(_log))
    print(len(_log))


def _read_retained_log():
    '''This is the new version of "_get_retained_message()", that was
    a function which only reads the retained topic. Now, it'll read the
    chat topic, that is the retained topic instead.'''
    with open('intranet_chat_log.txt', 'r', encoding='utf8') as file:
        nt_log = json.load(file)
    
    # Eval should identify this big str list into a normal list.
    # Probably it's easier to implement than a list.strip
    global _log
    _log = ast.literal_eval(str(nt_log))
    # type_debug()


def on_connect(client, userdata, flags, rc, propeties):
    client.subscribe(MQTT_LOG)
    _read_retained_log()


def _update_messages_on_log():
    """ This function will always remove the first index of the log."""
    if len(_log) > 49:
        _log.__delitem__(0)
    print()


def on_message(client, userdata, msg):
    """ This function is a callback that returns everytime we receive a new
    message into the mqtt topic that we are subscribed at this moment."""
    message_value = str(msg.payload)[2:-1]

    if chat_page.page_state:
        _show_log()
        print('\n', _command_str)
    
    if not _log:
        _log.append(message_value)

    #elif _log[-1] != message_value:
     #   _log.append(message_value)
    
    with open('intranet_chat_log.txt', 'w', encoding='utf8') as file:
        json.dump(_log, file, ensure_ascii=False)
    

def _show_log():
    with open('intranet_chat_log.txt', 'r', encoding="utf8") as file:
        _log = json.load(file)
        for messages in _log:
            print(messages)
        print(_f_msg)
        

def _send_log():
    """ If we want only to see the log, we can call this function """
    while True:
        with open('intranet_chat_log.txt', 'r', encoding='utf8') as file:
            messages_on_log = json.load(file)
            for messages in messages_on_log:
                print(messages)
            print()

        decision_input = input("Do you wanna leave the log? [yes]-[leave]-[sure]-[no] ")
        if decision_input in ['yes','leave','sure']:
            log_page.page_state = False
            chat_page.page_state = False
            clean_terminal()
            break

        else:
            _send_log()


def _publish_retained():
    with open('intranet_chat_log.txt', 'w') as file1:
        json.dump(_log, file1, indent=0, ensure_ascii=False)
    publish.single(
            topic= MQTT_LOG,
        hostname= MQTT_HOST,
            post= MQTT_PORT,
         payload= str(_log),
                 retain=True
    )


def _send_message():
    _terminal_break = 'clear ; python -u'
    print(_command_str)
    while True:
        try:
            _msg_input = input()
            clean_terminal()
            if _msg_input in ['', (len(_msg_input)*" ")] or len(_msg_input) in range(0,2):
                clean_terminal()
                print("Your message is quite short, please write something bigger. ")
                print(_command_str)
                continue
            
            global _f_msg
            _f_msg = f"[{_actual_datetime}] {UserLoginModuleNEW._username_variable}: {_msg_input}"

            if _msg_input in ['!leave', '!exit']:
                log_page.page_state = False
                chat_page.page_state = False
                clean_terminal()
                break

        except KeyboardInterrupt():
            _publish_retained()
            user_logout("Keyboard Interrupt caused by user. Exiting the program")

        if _terminal_break in _msg_input:
            clean_terminal()
            _publish_retained()
            user_logout("The program cannot run with two instances of itself. Exiting the program.")

        _log.append(_f_msg)
        publish.single(
               topic= MQTT_LOG,
            hostname= MQTT_HOST,
                port= MQTT_PORT,
                payload= str(_log),
                     retain=True
        )
        lambda: _publish_retained()
        lambda: _update_messages_on_log()

def _starter_page():
    """ Basically the first screen that will be opened to us """
    while True:
        if UserLoginModuleNEW._username_variable != "":
            break
            
        _action = input("What do you want to do? [login]-[register] ").lower()

        _callable_actions = {'login': lambda: user_login(),
            'register': lambda: UserCreation.user_and_password_register()}
        
        _do_action = _callable_actions.get(_action) if _callable_actions.get(_action) is not None\
                    else print("Command not registered, try again.")
        try:
            _do_action()
        except TypeError:
            clean_terminal()
            print("Non recognized command.")
        continue


def _exec(*func):
    for f in func:
        f()
    return


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.connect(MQTT_HOST, MQTT_PORT)
client.loop_start()
client.on_message = on_message
_stop = client.loop_stop


def main():
    """ This is the main function, were we estabilish the connection commands, the communication
    connection and the start of the MQTT search loop. Also, here we have the User command input."""
    log_page.page_state = False
    chat_page.page_state = False
    clean_terminal()
    _starter_page()
    while True:
        _command = input("Commands: [chats]-[log]-[logout]-[leave] ")
        print()

        try:
            _command_action = _callable_objects[_command.lower()]._show_page() if _callable_objects[_command.lower()]._show_page()\
                                is not None else ...
            _command_action()

        except (TypeError, KeyError):
            if _command not in _callable_objects and _command in ['leave', 'exit']:
                _publish_retained()
                sys.exit("Leaving due to user order. ")
            else:
                print('Command not defined.')
                clean_terminal()


if __name__ in "__main__":
    main()       