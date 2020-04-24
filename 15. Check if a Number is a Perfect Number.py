# This is a Python Program to check if a number is a Perfect number.

n = int(input("\nEnter any Number = "))

tot = 0
for i in range (1, n):
    if (n%i == 0):
        tot += i

print("---------------------------")
if (tot == n):
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")
print("---------------------------")