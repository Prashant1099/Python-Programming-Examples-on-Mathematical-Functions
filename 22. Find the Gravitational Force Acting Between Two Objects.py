# This is a Python Program to find the gravitational force acting between two objects.
# formula F = (G*m1*m2)/(r**2) N where G = 6.67 * 10^(-11)

m1 = float(input("\nEnter Mass of First Object  = "))
m2 = float(input("Enter Mass of Second Object = "))
r = float(input("Enter Distance between two Objects = "))

G = 6.67 * (10**-11)
F = (G*m1*m2)/(r**2)

print('-----------------------------')
print("Gravitational Force = ",round(F,2),"N")
print('-----------------------------')