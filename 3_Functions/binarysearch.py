def search(low, high):
	current_guess = low + (high-low)//2
	
	invalid_response = True
	while (invalid_response):
		response = input("Is your number " + str(current_guess)+ ":")
		if response == 'y':
			print("Great! I knew I could do it")
			return
		elif response == 'n':
			invalid_response = False
		else:
			print("I couldn't understand that")
		
	
	invalid_response = True
	while (invalid_response):
		response = input("Is it less than " + str(current_guess) + "(yes/no):")
		if response == 'yes':
			print("Hmm...")
			search(low, current_guess-1)
			invalid_response = False
		elif response == 'no':
			print("Hmm...")
			search(current_guess+1,high)
			invalid_response = False
		else:
			print("I couldn't understand that")

print("I can guess your number in 10 or less moves!")
print("In your head, pick a number between 0 and 1000, and I'll try to guess it.")
print("Ready?")
search(0,1000)