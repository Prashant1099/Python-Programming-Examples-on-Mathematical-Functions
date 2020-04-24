# The program takes in a year and checks whether it is a leap year or not.

y = int(input("\nEnter any Year = "))

print("-------------------------------")
if (y%4 == 0 and y%100 != 0 or y%400 == 0): # The if statement checks if the year is a multiple 
    print(y,"is a Leap Year")               # of 4 but isn’t a multiple of 100 or if it is a 
else:                                       # multiple of 400 (not every year that is a multiple 
    print(y,"is a not a Leap Year")         # of 4 is a leap year).
print("-------------------------------")