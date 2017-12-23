import re

""" 
This regular expression finds any text with the pattern "Agent [some letters]".
The regex '\w' stands for "find any string of letters" and the '+' stands for
"the pattern must have one or more". Together, /w+ finds any text that has at
least one or more letters. This means it will find strings with "Agent [name]"
but it will NOT find strings with just "Agent".
"""
namesRegex = re.compile(r'Agent \w+')
originalStr = 'Agent Alice gave the secret documents to Agent Bob.'
censoredStr = namesRegex.sub('CENSORED', originalStr)
print('Original Message: ' + originalStr)
print('Censored Message: ' + censoredStr)

