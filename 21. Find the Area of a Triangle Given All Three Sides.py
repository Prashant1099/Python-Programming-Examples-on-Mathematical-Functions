# This is a Python Program to find the area of a triangle given all three sides.

import math

a = int(input("\nEnter First Side  = "))
b = int(input("Enter Second Side = "))
c = int(input("Enter Third Side  = "))

s = (a+b+c)/2
ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("-------------------------------------------------")
print("Area of Triangle having sides {0},{1} and {2} = {3}".format(a,b,c,round(ar,2)))
print("-------------------------------------------------")