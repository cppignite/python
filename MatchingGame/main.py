from random import randint

def main():
    won = False
    hiddenarray = ['x'] * 10
    array = initarray()
    while not won:
        printarray(hiddenarray)
        first = int(input("Enter number of 1st card: ")) - 1
        hiddenarray[first] = array[first]
        printarray(hiddenarray)
        second = int(input("Enter number of 2nd card: ")) - 1
        hiddenarray[second] = array[second]
        printarray(hiddenarray)
        if hiddenarray[first] != hiddenarray[second]:
            hiddenarray[first] = 'x'
            hiddenarray[second] = 'x'
        won = checkarray(hiddenarray)
    print("\nCongrats! You won!")

def checkarray(array):
    good = True
    for i in range(0, len(array)):
        if array[i] == 'x':
            good = False
    return good

def initarray():
    list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    arr = [0] * 10
    i = 0
    while len(list) > 0:
        num = randint(0, len(list) - 1)
        arr[i] = list[num]
        del list[num]
        i = i + 1
    return arr

def printarray(array):
    print("")
    print(" ".join(str(x) for x in range(1, len(array) + 1)))
    print(" ".join(str(x) for x in array))

main()