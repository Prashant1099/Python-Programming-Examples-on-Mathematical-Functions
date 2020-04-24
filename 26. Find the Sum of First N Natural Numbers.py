# This is a Python Program to find the sum of first N Natural Numbers.

r = int(input("\nEnter any Range = "))

sum = 0
for i in range (1, r+1):
    sum += i

# print("----------------------------------------")
# print("Sum of first {0} Natural Numbers = {1}".format(r,sum))
# print("----------------------------------------")

print("----------------------------------------")
print("Sum of series: ", end="")
for i in range (1, r+1):
    if (i<r):
        print(i, end="+")
    else:
        print(i, end=" = ")
print(round(sum,2))
print("----------------------------------------")