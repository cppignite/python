# Raising an exception for improper amount of jelly beans

def verifyJellyBeans(numberOfJB):
  if (numberOfJB < 0):
    raise Exception('Jelly Beans cannot have a non-negative number')
  return numberOfJB

while True:
  try:
    verifyJellyBeans(int(input('How many Jelly Beans do you have? ')))
  except Exception as err:
    print('An exception happened: ' + str(err))
