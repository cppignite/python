#! /usr/bin/python3
"""
  The requests module allows you to download files from the Web.

  functions used:
  requests.get() takes a string of a URL to download. - Returns a Response
                 object which contains the response the web server gave to
                 your request

  res.status_code and requests.codes.ok check if the request was successful
  len(res.text) shows how many characters
  res.text is list of words of the text
  res.raise_for_status() - raises an exception if fail
"""

import pyperclip

weburl = pyperclip.paste()
res = requests.get(weburl)

if res.status_code == requests.codes.ok:
  print('Request Successful')
