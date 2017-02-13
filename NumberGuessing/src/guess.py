import random

def checkGuess(n):
	if (n > number):
		print("Too high!\n")
		return False
	elif (n < number):
		print("Too low...\n")
		return False
	elif (n == number):
		print("You got it!\n")
		return True

def main():
	global number 
	number = random.randint(1, 100)

	print(number) #Debugging
	print("Guess a number from 1-100!")

	done = False

	while (done != True):
		guess = input("Enter a number: ")
		done = checkGuess(int(guess))


if __name__ == '__main__':
	main()
