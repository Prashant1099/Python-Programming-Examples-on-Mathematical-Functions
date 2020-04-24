# This is a Python Program to check if a totber is a strong totber.
# Strong totber is the totber whose sum of factorial of the digits in any totber is equal to the given totber.
# 45, 40585 are Strong Numbers.

n = int(input("\nEnter any Number = "))

tot = 0
temp = n
while (n>0):
    i = f = 1
    mod = n%10
    while (i<=mod):
        f *= i
        i += 1
    tot += f
    n //= 10

print("---------------------------")
if (temp == tot):
    print(temp,"is a Strong Number")
else:
    print(temp,"is not a Strong Number")
print("---------------------------")