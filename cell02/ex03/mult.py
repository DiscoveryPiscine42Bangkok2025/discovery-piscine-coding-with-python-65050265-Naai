num1 = float(input('Enter a first number:'))
num2 = float(input('Enter a second number:'))
mult = num1 * num2
if mult < 0:
   print('This number is negative.')
elif mult > 0:
   print('This number is positive.')
else:
   print('This number is both positive and negative.')