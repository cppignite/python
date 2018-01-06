lockedDoor = False

def leaveHouse():
  lockedDoor = True

print('I am going to leave my house')
assert lockedDoor == True, 'You did not lock your doors before leaving!'
# Now I know to lock my door
