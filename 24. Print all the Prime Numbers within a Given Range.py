# This is a Python Program to print all prime numbers within a given range.

r = int(input("\nEnter any Range = "))

print("---------------------------------")
print("Prime Numbers upto range {0} are:".format(r))
print("---------------------------------")
for i in range (1, r+1):
    count = 0
    n = i
    for j in range (2, n+1):
        if (n%j == 0):
            count += 1

    if (count == 1):
        print(n)
print("---------------------------------")            