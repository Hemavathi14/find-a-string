#pattern
def pattern1(n):
    for i in range (1,n+1):
        for j in range (i,i+1):
            print(j,end = "")
        print()

n = int(input("Enter a number: "))
pattern1(n)
# p    to print like this
# py
# pyt
# pyth
# pytho
# python

n = input("Enter a string: ")
length = len(n)
for i in range (1,length+1):
    print(n[:i])

