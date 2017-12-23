#! /usr/bin/python3
"""
passwordLocker.py - An insecure password locker program.
*Make sure you use pip to install pyperclip beforehand
1.) Choose data structure - We will store name and password into a dictionary
                            as a key-value pair
2.) Handle Command Line Arguments - sys.argv is a list where the first item is
                                    the name of the program and the second item
                                    is the first command line argument
3.) Copy the right password 
    a.) See if the account exists in the PASSWORDS dictionary as a key 
       i.) If so, copy the key's value to the clipboard. (remember to import
           pyperclip so you can use pyperclip.copy()). We don't need the
           account variable because we could just use sys.argv[1]

"""
PASSWORDS = {'email': 'test',
             'blog': 'test1'
             'luggage': 'test2'}

import sys, pyperclip
if len(sys.argv) < 2:
  print('Usage: python passwordLocker.py [account] - copy account password')
  sys.exit()

account = sys.argv[1]  # first command line arg is the account name
