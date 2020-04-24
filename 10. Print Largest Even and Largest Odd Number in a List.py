# This is a Python Program to print the largest even and largest odd number in a list.

r = int(input("\nEnter Range = "))
a = []

for i in range (r):
    n = int(input("Enter Element {0} = ".format(i+1)))
    a.append(n)

max_even = max_odd = a[0]
for element in a:
    if element > 0:
        if element%2 == 0:
            if element > max_even:
                max_even = element
        else:
            if element > max_odd:
                max_odd = element

print("----------------------------------")
print("Largest Even Number in List = ",max_even)            
print("Largest Odd Number in List  = ",max_odd)                
print("----------------------------------")