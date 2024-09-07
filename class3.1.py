'''Write a python program to print the string S with every character except vowels 
in S '''
S=input("ENTER A STRING: ")
for i in range(len(S)):
    if S[i] not in ['a','e','i','o','u','A','I','O','U','E']:
        S=S.replace(S[i],'_')
print(S)