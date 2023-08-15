# multiplication table of N
num = int(input('Enter the number to print its multiplication table'))

for i in range(1, 11):
    product = num * i
    print(f'{num} X {i} = {product}')