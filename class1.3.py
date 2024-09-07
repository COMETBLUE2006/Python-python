'''finding vowel and consonants'''
alphabet=input("Enter a character")
if len(alphabet)==1:
    if alphabet==('a'or'e'or'i'or'o'or'u'or'A'or'E'or'U'or'O'or'I'):
        print(alphabet,"is vowel")
    else:
        print(alphabet,"is consonant")
else:
    print("Enter only one character")