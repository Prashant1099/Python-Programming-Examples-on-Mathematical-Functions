# This is a Python Program to take the temperature in celsius and convert it to Fahrenheit.

cel = float(input("\nEnter temperature in Celsius = "))

fah = (cel * (9/5)) + 32

print("----------------------------------")
print(cel,"Celsius = ", round(fah,2),"Fahrenheit")
print("----------------------------------")