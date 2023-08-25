a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

if a > b:
    if a > c:
        print(f"{a} is Largest")
    else:
        print(f"{c} is Largest")
elif b > c:
    print(f"{b} is Largest")
else:
    print(f"{c} is Largest")
