vocabList = ["",""] #initialize a empty list of size 2

#naive approach 1
vocabList[0] = input("Please put in an adj: ")
vocabList[1] = input("Please put in an adj: ")
print("You are in a " + vocabList[0] + " forest, and you are " + vocabList[1] + ".")
#problems: Rigid length, cumbersome to type it all out

#naive approach 2
for x in range(0, desiredNumber):
    vocabList[x] = input("Please put an adj: ");
print("You are in a " + vocabList[0] + " forest, and you are " + vocabList[1] + ".")
#problem: still typing it out

#proper approach
for x in range(0, desiredNumber):
    vocabList[x] = input("Please put an adj: ");
story = "You are in a {} forest, and you are {}."
print(story.format(*vocabList))

#transition into fileIO
requests = ["noun","verb","verb"]
for x in range(0,len(requests)):
    vocabList.append(input(requests[x]))
story = "A {} is often great at {} and {}."
print(story.format(*vocabList))

input("Press Enter to Quit") 

