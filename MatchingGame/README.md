# Handout #4

Here are some exercises to practice the core concepts that we will be covering this week.

#### Using arrays

~~~~
#Creates an array (named myArray) which contains the values "hello" , "world" , and "!"
myArray = ["hello", "world", "!"]

#Prints the length of the array
length = len(myArray)
print(length) #prints 3
~~~~

~~~~
#Creates an array (named arr) of 5 numbers, all of which are of the value 0
arr = [0] * 5

#Get the value at the index 2 of the array and set the variable num to equal that value
num = arr[2]

#Set the value at the index 0 of the array to equal 5
myNum = 5
arr[0] = myNum

#To go through all of the values in the array (known as "iterating" through the array)
for i in arr:
	print(i)
	
#Another way to iterate through the array
for i in range(0, len(arr)):
	print(i)
~~~~

#### Using 'for' loops

~~~~
#Prints 1 through 5
for i in range(5):
    print(i)
~~~~

~~~~
counter = 1
array = [0] * 5 #Creates an array of 5 numbers, all of which are of the value 0

#What does this print?
for i in array:
    print(i + counter)
	counter = counter + 1
~~~~

#### Using the String.join() method

~~~~
//Output: a-b-c
s = "-";
seq = ("a", "b", "c"); #This is sequence of strings.
print s.join(seq)
~~~~

~~~~
//Useful for printing out a list of numbers on 1 line
//Output: 1 2 3 4 5 6 7 8 9
print(" ".join(str(x) for x in range(1, 10)))
~~~~

~~~~
//Output: hey hey hey hey hey
array = ["hey"] * 5
print(" ".join(str(x) for x in array))
~~~~


#### Using 'while' loops

~~~~
for i in range(10):
    print(i)
    
i = 0
while i < 10:
    print(i)
    i = i + 1    #Alternatively: i += 1
~~~~

~~~~
#This is known as an infinite loop
done = True
while done:
    print("This will happen forever...")
	
print("This statement will never be printed")
~~~~

~~~~
done = False
while not done:
    userInput = input("To exit the loop, type "yes": ")
    if userInput == "yes":
        done = True #make sure to always have some condition to end the while loop
	else:
		print("I will now ask you again lol")
print("Now you're out of the loop")
~~~~

#### Using random numbers/integers

~~~~
#Imports the method randint from the random class
from random import randint

#Instantiate a variable named num with a random integer between 1 and 10
num = randint(1, 10) #the randint method parameters are both inclusive
~~~~

#### User-defined functions/methods

Functions and methods are the same in this context, and I will be using the words interchangably.

~~~~
#Output: Hello world!
def helloWorld():
    print("Hello world!")
    
helloWorld()
~~~~

~~~~
#Prints out the square of an integer entered by the user.
#num is called a parameter, which means it is some variable that is passed
#into the function through the function call
def squareInteger(num):
    print(num * num)
    
#python considers the user's input to be a String, so convert the String to an integer
#with the int() method
myNum = int(input("Enter a number: "))

#notice that myNum is passed into the squareInteger function as a parameter.
#now the squareInteger function can use that variable however it wants
#(in this case it will multiply the number by itself and then print the result)
squareInteger(myNum)
~~~~

~~~~
#Methods can return values/variables. This method takes a number as a parameter,
#then returns the square of that number
def squareInteger(num):
    return num * num

myNum = int(input("Enter a number: "))
squaredNum = squareInteger(myNum)
print(squaredNum)
~~~~

~~~~
#What does this print out?
def main():
	addBorder()
	print("HELLO")
	addBorder()
	print("WORLD")
	addBorder()

def addBorder():
    print("")
	print("=======")
	print("")

main()
~~~~

~~~~
//What does this program do?
//Notice that different methods use the same variable names, even though each
//variable is unique to the method that it is in
def main():
	size = int(input("Choose size of array: "))
	array = createArray(size)
	printArray(array)
	
def createArray(size):
	array = [0] * size
	return array
	
def printArray(array):
	for i in range (0, len(array)):
		print(array[i])

main()
~~~~

~~~~
def a():
    b()
    print("A")

def b():
    c()
    print("B")

def c():
    print("C")
    
a()
~~~~
