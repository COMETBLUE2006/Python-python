#write a program to calculate the sum of a series upto n terms
n=int(input("Enter no. of terms"))
sum=0
term=0
for i in range(n):
    term=term*10+2
    sum+=term
print("SUM OF TERMS IS:",sum)