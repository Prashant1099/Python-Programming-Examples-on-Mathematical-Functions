# This is a Python Program to find the LCM of two numbers.

n1 = int(input("\nEnter First Number  = "))
n2 = int(input("Enter Second Number = "))

if (n1>n2):
    max = n1
else:
    max = n2

print("------------------------")
while (1):
    if (max%n1 == 0 and max%n2 == 0):
        print("LCM of {0} and {1} = {2} ".format(n1,n2,max))
        break
    max += 1
print("------------------------")