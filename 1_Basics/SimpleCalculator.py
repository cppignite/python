#Let's make a simple calculator program that uses what we've learned so far!

print('Welcome to the simple Calculator program. \n You will first be able to add, then multiply, then divide!')

print("Let's add!")
print("What's the first number for the addition?")
firstNum = int(input())
print("What's the second number for the addition?")
secondNum = int(input())

print (firstNum + " + " + secondNum + " = " + str(firstNum + secondNum)) #This will give us an error..but Why?

#Let's fix the error!

print (str(firstNum) + " + " + str(secondNum) + " = " + str(firstNum + secondNum))  #Much better!




print("Let's Multiply!")
print("What's the first number for the multiplication?")
firstNum = int(input())
print("What's the second number for the multiplication?")
secondNum = int(input())

print (str(firstNum) + " * " + str(secondNum) + " = " + str(firstNum ** secondNum)) #This answer is wrong..but Why?

#Let's fix the error!

print (str(firstNum) + " * " + str(secondNum) + " = " + str(firstNum * secondNum))  #Much better!




print("Let's Divide!")
print("What's the first number for the Division?")
firstNum = float(input())
print("What's the second number for the Division?")
secondNum = float(input())

print (str(firstNum) + " / " + str(secondNum) + " = " + str(firstNum // secondNum)) #This answer will most likely be wrong...but Why?

#Let's fix the error!

print (str(firstNum) + " / " + str(secondNum) + " = " + str(firstNum / secondNum))  #Much better!


