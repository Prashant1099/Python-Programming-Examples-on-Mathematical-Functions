# This is a Python Program to generate all the divisors of an integer.

n = int(input("\nEnter any Number = "))

print("-------------------------------")
print("All Divisors of {0} are:".format(n))
print("-------------------------------")
for i in range (1, n+1):
    if n%i == 0:
        print(i)
print("-------------------------------")