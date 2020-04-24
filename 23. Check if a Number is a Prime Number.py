# This is a Python Program to check if a number is a prime number.

n = int(input("\nEnter any Number = "))

print('-------------------------')
for i in range (2, n):
    if (n%i == 0):
        print(n,"is not a Prime Number")
        break
else:
    print(n,"is a Prime Number")
print('-------------------------')

# print('-------------------------')
# count = 0
# for i in range (1, n+1):
#     if (n%i == 0):
#         count += 1
    
# if (count==2):
#     print(n,"is a Prime Number")
# else:
#     print(n,"is not a Prime Number")
# print('-------------------------')