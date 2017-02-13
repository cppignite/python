# Handout #3

Before we get started, here are a couple of exercises to practice loops and functions.

#### Using 'for' loops

~~~~
for i in range(5):
    print(i, "- Hello!")
~~~~

~~~~
for i in range(2,12,2):
    print(i)
~~~~

~~~~
#What will the output be?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("done")
~~~~

~~~~
total = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    if new_number == 0:
        total += 1
print("You entered a total of ", total, " zeroes.")
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
while(True): #What happens if we use 'False' instead?
    print("This will happen forever...")
~~~~

~~~~
done = False
while not done:
    quit = input("Do you want to quit? (y/n) ")
    if quit == "y":
        done = True
    
    attack = input("Does your mage cast fireball on the Demogorgon? (y/n) ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True
~~~~

#### Using random numbers

~~~~
import random

my_number = random.randrange(50)

my_number = random.randrange(100, 201)
~~~~

#### User-defined functions

~~~~
def printHello():
    print("Hello!")
    
printHello()
~~~~

~~~~
def printThis(word):
    print(word)
    
word = input("Enter a string: ")
printThis(word)
~~~~

~~~~
def inner_function():
    print("inner")

def outer_function():
    print("outer")
    inner_function()
    
outer_function()
inner_function()
~~~~

~~~~
def getNumber():
    return 5
    
five = getNumber()
print(five)
~~~~

~~~~
def add(a, b):
    result = a + b
    return result

a = 2
b = 3
print(add(a,b))

c = 3
d = 4
cd = add(c,d)
print(cd)
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
