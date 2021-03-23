print("Enter three numbers to find the smallest one")

a = input("Enter first number")
b = input("Enter second number")
c = input("Enter third number")

if a<b:
    if a<c:
        print(a," is smallest")
    else:
        print(c," is smallest")
else:
    if b<c:
        print(b," is smallest")
    else:
        print(c," is smallest")
    
