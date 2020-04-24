# This is a Python Program to find those numbers which are divisible by 7 and multiple of 5 in a given range of numbers.

lr = int(input("\nEnter Lower Range = "))
ur = int(input("Enter Upper Range = "))

print("-----------------------")
for num in range (lr, ur+1):
    if (num%7 == 0 and num%5 == 0):
        print(num)
print("-----------------------")
