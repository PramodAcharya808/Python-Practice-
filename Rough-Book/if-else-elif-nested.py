num = int(input('Enter a number: '))
if num < 0:
    print('Entered number is Negative')
elif num > 0:
    if 5 <= num <= 10:
        print('Number lies between 5 to 10')
    else:
        print('Number OutOfBound')
else:
    print('Number entered is ZERO (0)')