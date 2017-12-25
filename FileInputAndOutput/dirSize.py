#! /usr/bin/python3
# Finds the total size of current directory in bytes
import os

totalSize = 0
for filename in os.listdir(os.getcwd()):
  totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))
print('The total size of the current directory is ' + str(totalSize) + ' bytes.')

# convert to kilobytes, megabytes, and gigabytes
