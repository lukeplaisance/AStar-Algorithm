#pylint: disable = E1101
#pylint: disable = C0330
from random import *

def password():
    '''function to generato password'''
    f = open("passwords.txt", "r")
    password = []
    current_list = []
    for word in f:
        word = word.replace("\n", "")
        password.append(word)
    for word in f:
        word = word.replace("a", "@")
        password.append(word)

    print password

password()