#! /usr/bin/python3
"""
Description: 
  Say you're a geography teacher with 35 students in your class and you want to
  give a pop quiz on US state capitals. Alas, your class has a few bad eggs in
  it, and you can't trust the students not to cheat. You'd like to randomize
  the order of questions so that each quiz is unique, making it impossible for 
  anyone to crib answers from anyone else. Of course, doing this by hand would
  be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:
  * Creates 35 different quizzes (35 for number of students)
  * Creates 50 multiple-choide questions for each quiz, in random order.
    (50 for the amount of states in the US)
  * Proives the correct answer and three random wrong answers for each question,
    in  random order
  * Writes the quizzes to 35 text files
    This means the code will do the following:
     ** Store the states and their capitals in a dictionary
     ** Call open(), write(), and close() for the quiz and answer key text
        files
     ** Use random.shuffle() to randomize the order of the questions and
        multiple-choice options.

Extensions:
  * Create a Text User Interface allowing how many questions to use and how
    many tests to generate
  * Ask what to name exam
  * Make it so the teacher can input any question and answer on a text document
    and the program will read from that document to generate the dictionary.
    ** Adapt Text User Interface to ask for file input of the questions and ans
  * Create a Graphical User Interface
"""
# Step 0: Import modules
import random, re, os

# Step 1: Store the Quiz Data in a Dictionary
def readQuizData():
  testFile = open('key.txt')
  rawData = testFile.readlines() # stores each line in a list
  
  testRegex = re.compile(r'''
              ([^,]+) # question,         (.+) the wild card regex finds 
              ,       # comma seperator   anything except a new line character
              (.+)    # answer            [^,] finds anything except the comma
              ''', re.VERBOSE)
  # Find matches in text document
  
  matches = {}
  for i in rawData:
    info = testRegex.search(i)
    matches[info.group(1)] = info.group(2)
  return matches 

capitals = readQuizData()

# Step 2: Create the Quiz File and Shuffle The Question Order
# Generate x=35 quiz files
os.makedirs('exams')    # makes 'exam' folder
os.makedirs('answers')  # makes 'answers' folder
numOfExams = 35
for quizNum in range(numOfExams):
  # Create the quiz and answer key files
  quizFile = open('exams/capitalsquiz%s.txt' % (quizNum + 1), 'w')
  answerKeyFile = open('answers/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

  # Write out the header for the quiz
  quizFile.write('Name:\n\nDate:\n\n')
  quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
  quizFile.write('\n\n')

  # Shuffle the order of the states.
  states = list(capitals.keys())
  random.shuffle(states)

# Step 3: Create the Answer Options
# Loop through all 50 states, making a question for each
  for questionNum in range(50):

    # Get right and wrong answers.
    # Get correct answer from our capitals dictionary
    correctAnswer = capitals[states[questionNum]]
    # Duplicate all of the answers of the capitals dictionary
    wrongAnswers = list(capitals.values())
    # Delete the correct answer from the wrongAnswers list
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    # Select three random wrong answers
    wrongAnswers = random.sample(wrongAnswers, 3)
    # Add in correct answer for our 4 possible answers to a question
    answerOptions = wrongAnswers + [correctAnswer]
    # Randomize the answer options to the correct answer isn't D
    random.shuffle(answerOptions)

# Step 4: Write content to Quiz and Answer Key Files
    # Write the question and the answer options to the quiz file
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, 
                   states[questionNum]))
    for i in range(4):
      quizFile.write('    %s. %s \n' % ('ABCD'[i], answerOptions[i]))
    quizFile.write('\n')

    # Write the answer key to a file
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
                        answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
