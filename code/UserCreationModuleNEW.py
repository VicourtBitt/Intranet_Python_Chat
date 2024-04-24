"""
This module has been created to help the User to register itself,
saving the registered data into a JSON file.

Created by VicourtBitt, used in PyChat/Intranet Chat Project.
GitHub: https://github.com/VicourtBitt/Intranet_Python_Chat
"""

# Built-in Python Modules
import json
from datetime import datetime

# Third-Party Python Modules
from paho.mqtt import publish

# Self-Made Python Modules
from CleanTerminalModule import clean_terminal
from getmac import get_mac_address as gma

_mac_value = gma()
_creation_moment = datetime.now().strftime('%d/%m - %H:%M')

_intranet_users = {}


def _gather_intranet_users():
    """Function meant to recall the users dict."""
    with open('intranet_login_df.txt', 'r', encoding='utf8') as file:
        global _intranet_users
        _intranet_users = json.load(file)
        print("Recovering Data...")
    return _intranet_users


def _save_intranet_users():
    """This saves the new registered user into the json file."""
    with open('intranet_login_df.txt', 'w', encoding='utf8') as file:
        json.dump(_intranet_users, file,indent=2, ensure_ascii=False)
        print("Saving the users dataframe...")


def _non_usable_lenght(var, name):
    """This function make sure that the password will be at least 4 digits long."""
    if len(var) <= 3:
        print(f"The {name} need to have at least 4 digits long. ")
        return True
    return False


def _get_userdata():
    """This function gather all the relevant information from the user that is
    registering in the moment."""
    while True:
        _username_input = input("Write the USERNAME that you want to use: ")
        if _non_usable_lenght(_username_input, "USERNAME"):
            continue

        _user_in_dict = _username_input in _intranet_users.keys()
        if not _user_in_dict:
            clean_terminal()
            
            _password_creation = input("Create your password: ")
            if _non_usable_lenght(_password_creation, "PASSWORD"):
                continue

            _password_verification = input("Write the same password again: ")

            _pass_check = _password_creation == _password_verification

            while True:
                if _pass_check:
                    _intranet_users.update(
                        {_username_input:
                            {
                                'username': _username_input,
                         'password': _password_verification,
                          'Date Creation': _creation_moment,
                                   'MAC_ADDRESS': _mac_value
                            }
                        }
                    )
                    break
                else:
                    print("They are not the same, try again.")
                    _get_userdata()
            break
        print("User already registered in the system, try with other username"\
                                                ,'\n','Or contact the support.')
        

def _publish_update():
    """Call this func in the future, see it."""
    publish.single(
           topic= 'login-intranetchat',
        hostname= 'test.mosquitto.org',
                            port= 1883,
                          retain= True,
           payload= str(_intranet_users)
    )


class UserCreation:
    """This class will be used to create a user and save it in the code."""
    def __init__(self):
        ...

    @classmethod
    def _register_info(cls):
        _gather_intranet_users()
        _get_userdata()
        _save_intranet_users()
        _publish_update() # Last Update

# UserCreation._register_info()