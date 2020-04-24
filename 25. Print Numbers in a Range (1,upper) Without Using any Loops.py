# This is a Python Program to print all numbers in a range without using loops.

def PrintNumber(r):
    if (r>0):
        PrintNumber(r-1)
        print(r)

r = int(input("\nEnter any Range = "))
print("----------------------")
PrintNumber(r)
print("----------------------")