import time
current = time.strftime('%H : %M : %S')
print('Current time is: '+current)
hr = int(time.strftime('%H'))
if 0 <= hr < 12:
    print('Good Morning !')
elif 12 <= hr < 18:
