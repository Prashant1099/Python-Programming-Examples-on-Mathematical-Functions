# This is a Python Program to find the sum of series: 1 + 1/1! + 1/2! + …… 1/n!

r = int(input("\nEnter any Range = "))

sum = f = 1
for i in range (1, r):
    f *= i
    sum += 1/f

print("-------------------------------------------------------------------")
print("Sum of series: 1",end=" + ")
for i in range (1, r):
    if (i<r-1):
        print("1/{0}!".format(i), end=" + ")
    else:
        print("1/{0}!".format(i), end=" = ")
print(round(sum,2))
print("-------------------------------------------------------------------")
