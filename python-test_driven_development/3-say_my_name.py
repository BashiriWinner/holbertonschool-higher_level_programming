#!/usr/bin/python3
'''
This is the "3-say_my_name" module.
The example module supplies one function, def say_my_name().
'''


def say_my_name(first_name, last_name=""):
    '''
    say_my_name function that prints My name is <first name> <last name>
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

