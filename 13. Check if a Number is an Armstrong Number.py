# This is a Python Program to check if a number is an Armstrong number.

n = int(input("\nEnter any Number = "))

tot = dig = 0
temp = n

while (n>0):
    n //= 10
    dig += 1

n = temp

while (n>0):
    mod = n%10
    tot += mod**dig
    n //= 10

print("-------------------------------")
if (temp == tot):
    print(temp,"is a Armstrong Number")
else:
    print(temp,"is not a Armstrong Number")
print("-------------------------------")