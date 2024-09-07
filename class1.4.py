#greatest of three numbers 
x=int(input("Enter a number"))
y=int(input("Enter another number"))
z=int(input("Just 1 more :)"))
if(x>y>z)or(x>z>y):
    print("x is the greatest")
elif(y>x>z)or(y>z>x):
    print("y is the greatest")
else:
    print("z is the greatest")