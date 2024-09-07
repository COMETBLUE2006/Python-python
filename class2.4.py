#write a program to print fabonacci series 
f1=0
f2=1
print(f1)
print(f2)
fn=f1+f2
while(fn<50):
    fn=f1+f2
    f1=f2
    f2=fn
    print(fn)