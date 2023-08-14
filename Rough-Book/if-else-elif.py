percentage = float(input('Enter your percentage: '))
if percentage < 35:
    print('FAIL')
elif 35 <= percentage < 85:
    print('PASS')
elif 85 <= percentage <=100:
    print('DISTINCTION')
else:
    print('Opps... INVALID PERCENTAGE')