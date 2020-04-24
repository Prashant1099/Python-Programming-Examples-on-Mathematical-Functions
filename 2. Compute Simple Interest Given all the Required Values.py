# This is a Python Program to compute simple interest given all the required values.

amt = float(input("\nEnter Principle Amount = "))
r = float(input("Enter Rate              = "))
t = float(input("Enter Time              = "))

si = (amt * r * t)/100

print("-----------------------------")
print("Simple Interest = ", si)
print("-----------------------------")