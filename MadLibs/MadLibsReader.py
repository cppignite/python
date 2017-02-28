fileName = input("Please Input the file you want to read: ") #read from user input for fileName
target = open(fileName, "r") #open the desired MadLibsFile
fileContent = target.readlines() #read all lines
target.close() #close the file

vocabList = [] #initialize a empty list
vocabCount = int(fileContent[0]) # parse how many vocabs are needed.

if(vocabCount > 0): #if any are needed
    for x in range(1, vocabCount+1): # for every needed vocab
        vocabList.append(input("Please input a/an: " + fileContent[x])) #add to the list what the user input for the required
story = ""
for x in range(vocabCount+1, len(fileContent)) # for each line after we get the vocabList
    story = story + fileContent[x] #combine the remaining lines into story

print(story.format(*vocabList)) #replace placeholders with vocabs
input("Press Enter to Quit") 

