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
  * Make it so the teacher can input any question and answer on a text document
    and the program will read from that document to generate the dictionary.
    ** Adapt Text User Interface to ask for file input of the questions and ans
  * Create a Graphical User Interface
"""
