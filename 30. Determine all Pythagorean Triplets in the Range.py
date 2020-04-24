# This is a Python Program to determine all Pythagorean triplets till the upper limit.

r = int(input("\nEnter any Range = "))

print("----------------------------------------")
print("Pythagorous Triplets upto range {0} are:".format(r))
print("----------------------------------------")
for i in range (1, r+1):
    a = i
    for j in range (1, i+1):
        b = j
        for k in range (1, j+1):
            c = k
            if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2)):
                print("{0:3}, {1:3}, {2:3}".format(c,b,a))
print("----------------------------------------")



# import math
# def pythagorean_triplet(n):
#   for b in range(n):
#     for a in range(1, b):
#         c = math.sqrt( a * a + b * b)
#         if c % 1 == 0:
#             print(a, b, int(c))
            
# pythagorean_triplet(12)