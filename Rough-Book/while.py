day = int(input('Enter the day number in a week: '))
while day > 3:
    match day:
        case 1:
            print('MONDAY')
        case 2:
            print('TUESDAY')
        case 3:
            print('WEDNESDAY')
        case 4:
            print('THURSDAY')
        case 5:
            print('FRIDAY')
        case 6:
            print('SATURDAY')
        case 7:
            print('SUNDAY')
            print('Hurray ...Its WEEKEND')
        case _:
            print('Please enter a valid day !!')
