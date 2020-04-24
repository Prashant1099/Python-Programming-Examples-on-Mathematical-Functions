# This is a Python Program to check if two numbers are amicable numbers.
# Amicable numbers 2 alag alag numbers hote hai. Agar ek ke divisor ka sum dusra number and second ke divisor 
# ka sum first number ho to wo Amicable numbers hai

# The first few amicable pairs are: (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368) 

n1 = int(input("\nEnter First Number  = "))
n2 = int(input("Enter Second Number = "))

sum1 = sum2 = 0

for i in range (1, n1):
    if (n1%i == 0):
        sum1 += i

for i in range (1, n2):
    if (n2%i == 0):
        sum2 += i        

print("--------------------------------------")
if (sum1==n2 and sum2==n1):
    print(n1,n2,"are Amicable Numbers")
else:
    print(n1,"and",n2,"are not Amicable Numbers")
print("--------------------------------------")