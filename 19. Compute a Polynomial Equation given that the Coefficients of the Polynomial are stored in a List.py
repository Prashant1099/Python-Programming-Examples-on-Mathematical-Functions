# This is a Python Program to compute a polynomial equation given that the coefficients of the polynomial are stored in the list.

import math

po = int(input("\nEnter the highest power of equation = "))
lst = []
tot = 0
temp = po

for i in range (0, po+1):
    coeff = int(input("Enter Coefficient = "))
    lst.append(coeff)

x = int(input("\nEnter Value of x  = "))

for i in range (0, po+1):
    while (po>0):
        tot += (lst[i]*math.pow(x,po))
        break
    po -= 1 
tot += lst[-1]

po = temp
print("-----------------------------------------------------------")
print("Sum of ",sep="+", end="")
for i in range (0, po+1):
    while (po>0):
        print("{0}.{1}^{2}".format(lst[i], x, po), end=" + ")
        break
    po -= 1
print(lst[-1]," = ",tot)
print("-----------------------------------------------------------")