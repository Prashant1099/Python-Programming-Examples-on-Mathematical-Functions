# This is a Python Program to print the table of a given number.

n = int(input("\nEnter any Number = "))

for i in range (1, 11):
    print("{0} x {1:<3} = {2:<3}".format(n,i,n*i))
    print("------------------")