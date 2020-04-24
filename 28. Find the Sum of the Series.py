# This is a Python Program to find the sum of series: 1 + x^2/2 + x^3/3 + … x^n/n.

r = int(input("\nEnter any Range  = "))
x = int(input("Enter Value of x = "))

sum = 1
po = 2
for i in range (2, r+1):
    po *= x         # po = x**i
    div = po/i
    sum += div

print("-------------------------------------------------------------------")
print("Sum of series: 1",end=" + ")
for i in range (2, r+1):
    if (i<r):
        print("({0}^{1})/{1}".format(x,i),end=" + ")
    else:
        print("({0}^{1})/{1}".format(x,i),end=" = ")
print(round(sum,2))
print("-------------------------------------------------------------------")