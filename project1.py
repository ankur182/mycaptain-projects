#wap which accepts radius of circle from user and compute area in python
from math import pi

r = float(input ("Enter radius of circle : "))
area=str(pi * r**2)

print ("Area of the circle is: " ,area)

#wap which accepts a filename from the user and print the extension of that
k= input("Enter Filename which is present in your folder: ")

f = k.split(".")

print ("Extension of the file is : " + f[-1])

