# This is a Python Program to read height in centimeters and then convert the height to feet and inches

cm = float(input("\nEnter Height in Centimeters = "))

ft = cm/(2.54*12)
inch = cm/2.54

print("-------------------------------")
print(cm,"centimeter = ",round(ft,2),"feet")
print(cm,"centimeter = ",round(inch,2),"inch")
print("-------------------------------")
