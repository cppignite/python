print('What is your name?')
name = input()
print('What is your password?')
password = input()
print('Thank you ' + name + '. System configured\n')

print('Who are you?')
if name == input():
  print('Welcome ' + name + '. What is your password?')
  if password == input():
      print('Access Granted')
  else:
      print('Access Denied')
else:
  print('Unauthorized Entry, you are not ' + name)
  


