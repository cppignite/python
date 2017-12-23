#! /usr/bin/python3
"""
passwordLocker.py - An insecure password locker program.
1.) Choose data structure - We will store name and password into a dictionary
                            as a key-value pair
2.) Handle Command Line Arguments - sys.argv is a list where the first item is
                                    the name of the program and the second item
                                    is the first command line argument

"""
PASSWORDS = {'email': 'test',
             'blog': 'test1'
             'luggage': 'test2'}

import sys
if len(sys.argv) < 2:
  print('Usage: python passwordLocker.py [account] - copy account password')
  sys.exit()

account = sys.argv[1]  # first command line arg is the account name
