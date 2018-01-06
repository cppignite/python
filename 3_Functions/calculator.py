def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b

def main():
	continue_program = True
	while (continue_program):
		display_menu()
		user_choice = input("Choice: ")
		# Students must first be taught that, in python, functions are first class citizens (they are treated as objects)
		# if this is too confusing for students, the program can be modified so that functions are not being passed.
		operation = get_operation_from_choice(user_choice)
		a = 0
		b = 0
		
		if operation != None:
			a,b = get_operands()
			if a != None: # alternatively, another exception can be raised and caught
				display_answer(a,b, operation)
		else:
			print("Your choice wasn't valid!")
		
		response = input("Do you want to calculate another value (y/n): ")
		if response == 'n':
			break
			
def display_menu():
	print("Choose which operation you want to do!")
	print("(a)dd")
	print("(s)ubtract")
	print("(d)ivide")
	print("(m)ultiply")

def get_operands():
	first = input("First Operand: ")
	second = input("Second Operand: ")
	
	try:
		a = int(first)
		b = int(second)
	except ValueError:
		print("One of those values is not a number!\n")
		return None, None
	
	return a,b

def get_operation_from_choice(user_choice):
		if user_choice == 'a':
			return add
		elif user_choice == 's':
			return subtract
		elif user_choice == 'm':
			return multiply
		elif user_choice == 'd':
			return divide
		else:
			return None

def display_answer(a, b, operation):
	print ("Answer: " + str(operation(a,b)))
	
main()