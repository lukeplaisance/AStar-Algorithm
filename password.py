#pylint: disable = E1101
#pylint: disable = C0330
from random import *

def password():
    '''function to generate password'''
    f = open("passwords.txt", "r")
    words = []
    for word in f:
        word = word.replace("\n", "")
        words.append(word)

    rand_word = randint(0,len(words) - 1)
    passwords = words[rand_word]
    print passwords

password()