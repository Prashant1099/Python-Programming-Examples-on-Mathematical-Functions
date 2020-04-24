# This is a Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.

r = int(input("\nEnter any Range = "))

temp = r
sum = 0
while (r>0):
    sum += 1/r
    r -= 1

print("-----------------------------------------------")
print("Sum of series: 1 + 1/2 + 1/3 +..+ 1/N = ",round(sum,3))
print("-----------------------------------------------")