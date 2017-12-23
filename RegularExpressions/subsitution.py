import re
namesRegex = re.compile(r'Agent \w+')
originalStr = 'Agent Alice gave the secret documents to Agent Bob.'
censoredStr = namesRegex.sub('CENSORED', originalStr)

print('Original Message: ' + originalStr)
print('Censored Message: ' + censoredStr)
