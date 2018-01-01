#! /usr/bin/python3
"""
 Script opens a google maps webpage with an address either on command line or
 on clipboard
 Demonstrates power of  webbrowser.open(url), which opens a web browser

 Usage: mapit <Address>
 Example: mapit 3801 W Temple Ave, Pomona, CA 91768

 Extra Projects: Open browser to what you usually open to
"""

import webbrowser, sys, pyperclip

# Step 1: Figure Out the URL
# The idea is that you can search by putting the address on the url of GMaps
if len(sys.argv) > 1:
  # Get Address from command line, we want to have the addr as a single string
  # We don't want the program name so we start from argv[1:]
  address = ' '.join(sys.argv[1:])

# Step 2: Handle the Command Line Arguments

# Step 3: Handle the Clipboard Content and Launch Browser
