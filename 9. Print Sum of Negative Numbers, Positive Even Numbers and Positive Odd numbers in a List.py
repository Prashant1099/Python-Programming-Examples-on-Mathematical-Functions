# This is a Python Program to print the sum of negative numbers, positive even numbers and positive odd numbers in a given 
# list.

r = int(input("\nEnter any Range = "))
a = []

print()
for i in range (r):
    n = int(input("Enter Number = "))
    a.append(n)

neg_sum = even_sum = odd_sum = 0
for element in range(len(a)):
    if a[element] < 0:
        neg_sum += a[element]
    elif a[element]%2 == 0:
        even_sum += a[element]
    else:
        odd_sum += a[element]

# for element in a:
#     if element > 0:
#         if element%2 == 0:
#             even_sum += element
#         else:
#             odd_sum += element
#     else:
#         neg_sum += element

print("---------------------------------------")
print("Sum of Negative Numbers      = ",neg_sum)
print("Sum of Positive Even Numbers = ",even_sum)
print("Sum of Positive Odd Numbers  = ",odd_sum)
print("---------------------------------------")