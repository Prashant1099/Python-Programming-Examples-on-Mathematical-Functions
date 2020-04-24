# This is a Python Program to form an integer that has the number of digits at the ten’s place and the least significant 
# digit in the one’s place.

n = int(input("\nEnter any Number = "))

dig = 0
mod = n%10
while (n>0):
    n //= 10
    dig += 1

print("------------------------")
print("New Formed Number = ",str(dig)+str(mod))
print("------------------------")


    