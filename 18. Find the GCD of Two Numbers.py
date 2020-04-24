# This is a Python Program to find the GCD of two numbers.

n1 = int(input("\nEnter First Number  = "))
n2 = int(input("Enter Second Number = "))

a = []

if (n1>n2):
    r = n1
else:
    r = n2

for i in range (2, r+1):
    if (n1%i == 0 and n2%i == 0):
        a.append(i)
        
print("------------------------")
print("GCD of {0} and {1} = {2}".format(n1,n2,a[-1]))
print("------------------------")

# import fractions
# print("The GCD of the two numbers is",fractions.gcd(n1,n2))
