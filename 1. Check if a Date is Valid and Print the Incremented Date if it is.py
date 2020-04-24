# This is a Python Program to check if a date is valid and print the incremented date if it is.

dd = int(input("\nEnter Date  = "))
mm = int(input("Enter Month = "))
yy = int(input("Enter Year  = "))


if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max = 31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    max = 30
elif (yy%4 == 0 and yy%100 !=0 or yy%400 ==0):
    max = 29
else:
    max = 28

print("-------------------------------")
print("Your Entered Date: {0}/{1}/{2}".format(dd,mm,yy))

if (dd<1 or dd>max or mm<1 or mm>12):
    print("Please Enter a valid Date!")
elif (dd==max and mm!=12):
    dd = 1
    mm += 1
    print("Incremented Date : {0}/{1}/{2}".format(dd,mm,yy))
elif (dd==max and mm==12):
    dd = 1
    mm = 1
    yy += 1
    print("Incremented Date : {0}/{1}/{2}".format(dd,mm,yy))
else:
    dd += 1
    print("Incremented Date : {0}/{1}/{2}".format(dd,mm,yy))
print("-------------------------------")