num = int(input('Enter number less than 25:'))
if num < 25:
    for i in range(num,26):
        print('Inside the loop, my variable is ',i)
    
else:
    print('Error')