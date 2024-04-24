"""
This module has been created to let the user login into the Intranet Chat,
this was implemented for security and identification purposes.

Created by VicourtBitt, used in PyChat/Intranet Chat Project.
GitHub: https://github.com/VicourtBitt/Intranet_Python_Chat
"""

# Built-in Python Modules 
import json
import sys

# Self-Made Python Modules
from CleanTerminalModule import clean_terminal

_username_variable = ""
_intranet_users_login = {}
_user_state = False


def _user_login_recover():
    """The program call this function to recover the JSON/CRUD DataFrame"""
    with open('intranet_login_df.txt', 'r', encoding='utf8') as file:
        global _intranet_users_login
        _intranet_users_login = json.load(file)
    return


def user_login(user= _username_variable, state= _user_state):
    """This is the user login function"""
    if user != "" and state == True:
        print("You still logged on, logout before trying to leave. ")
        return
    
    while True:
        _user_login_recover()
        user = input("Write your USERNAME: ")
        _user_in_df = user in _intranet_users_login.keys()

        if user in ['exit','leave','back']:
            sys.exit("Leaving the program due to user command. ")

        if not _user_in_df:
            clean_terminal()
            print("Wrong user or user not registered, try again. ")
            continue

        _password_input = input("Write your PASSWORD: ")
        _pass_verify = _password_input == (_intranet_users_login[user]['password'])

        if _pass_verify:
            global _username_variable
            _username_variable = user
            user_state = state
            clean_terminal()
            return print(f'Login wen successfully. Welcome {_username_variable}! ')
        
        if not _pass_verify:
            clean_terminal()
            print("Wrong password try again. ")


def user_logout(msg="Exiting the program. Due to order or an error."):
    """I guess it is self-explanatory, but it'll leave the program leaving the
    user to run the program again"""
    sys.exit(msg)
