#! /usr/bin/python3
"""
This project will take the phone numbers and email addresses from a webpage or
document and store it in a string.

Tasks of the program:
  * Get text off the clipboard
    - We can do this with pyperclip
  * Find all phone numbers and email addresses in text
    - We can create two regexes, one for phone numbers and one for emails
    - We need to find all matches, not just one match
  * Paste them onto the clipboard
    - We need to format the strings into a single string
    - Display some message if no matches were found

Remember: Break apart a big project into smaller problems and do them all
          seperately. That makes the project managable in terms you already
          know

We will use this script on some poor smuck's contact page

"""
# Step 0.) import pyperclip and regular expression modules
import pyperclip, re

# Step 1.) Create REGEX for phone numbers
phoneRegex = re.compile(r'''(
             (\d{3}|\(\d{3}\))?             # area code
             (\s|-|\.)?                     # seperator 
             (\d{3})                        # first 3 digits
             (\s|-|\.)                      # seperator
             (\d{4})                        # last 4 digits
             (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
             )''', re.VERBOSE)

# Step 2.) Create REGEX for email addresses
emailRegex = re.compile(r'''(
             [a-zA-Z0-9._%+-]+              # username
             @                              # @ symbol
             [a-zA-Z0-9.-]+                 # domain name
             (\.[a-zA-Z]{2-4})              # dot-something
             )''', re.VERBOSE)

# Step 3.) Find all matches in clipboard text
text = str(pyperclip.paste())
print(text)
matches = []
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # String building
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)
for groups in emailRegex.findall(text):
  matches.append(groups[0])

# Step 4.) Join the Matches into a String for the Clipboard
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipboard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')

