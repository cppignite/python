from random import randint
import os

def main():
    won = False
    size = 10  # number of cards
    hiddenarray = ['x'] * size
    array = initarray(size)
    while not won:
        printarray(hiddenarray)
        first = int(input("Enter number of 1st card: ")) - 1
        hiddenarray[first] = array[first]
        printarray(hiddenarray)
        second = int(input("Enter number of 2nd card: ")) - 1
        hiddenarray[second] = array[second]
        printarray(hiddenarray)
        if hiddenarray[first] != hiddenarray[second]:
            print("\nNo match!")
            hiddenarray[first] = 'x'
            hiddenarray[second] = 'x'
        won = checkarray(hiddenarray)
    print("\nCongrats! You won!")

def initarray(size):
    list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    array = [0] * size
    i = 0
    while len(list) > 0:
        num = randint(0, len(list) - 1)
        array[i] = list[num]
        del list[num]
        i = i + 1
    return array

def printarray(array):
    print("")
    print(" ".join(str(x) for x in range(1, len(array) + 1)))
    print(" ".join(str(x) for x in array))

def checkarray(array):
    good = True
    for x in range(0, len(array)):
        if array[x] == 'x':
            good = False
    return good

def clear():
    os.system('cls')

main()