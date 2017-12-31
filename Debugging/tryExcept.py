while True:
 numerator = int(input('Please enter a numerator: '))
 denominator = int(input('Please enter a denominator: '))
 try:
   print(str(numerator/denominator)) 
 except ZeroDivisionError:
   print('You cannot divide by zero. Try again...')

