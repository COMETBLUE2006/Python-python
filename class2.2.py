#write program to print a pattern
n=int(input("Enter the no. of rows:"))
for row in range(1,n+1):
    for col in range(n-row):
        print(" ",end='')
    for col in range(row):
        print("* ",end='')
    print("")