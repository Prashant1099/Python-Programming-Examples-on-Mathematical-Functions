# This is a Python Program to compute prime factors of an integer.

n = int(input("\nEnter any Number = "))


print("-------------------------")
print("Prime Factors of {0} are:".format(n))
print("-------------------------")
for i in range (2, n+1):
    if n%i == 0:
        count = 0
        for j in range (1, i+1):            
            if i%j == 0:
                count += 1
            
        if count == 2:
            print(j)
        
print("-------------------------")            