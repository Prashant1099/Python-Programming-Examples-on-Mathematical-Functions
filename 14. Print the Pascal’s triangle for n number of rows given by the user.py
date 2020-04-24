# This is a Python Program to print the pascal’s triangle for n number of rs given by the user. 

r = int(input("\nEnter number of rows = "))

print("-------------------------------")
print("Pascal's Triangle upto row: ",r)
print("-------------------------------")
e = 0
for row in range (1, r+1):
    for sp in range (r-row+1):
        print("  ", end="")

    n = 11**e
    e += 1

    while (n>0):
        mod = n%10
        print("  ",mod,end="")
        n //= 10
    print()
print("-------------------------------")