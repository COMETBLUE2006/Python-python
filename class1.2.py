# sum of the digits of a given number
num=int(input("Enter a number:"))
sum=0
while(num!=0):
    r=num%10
    num=num//10
    sum=sum+r
print("Sum of digits:",sum)