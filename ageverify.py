#!usr/bin/python3

import datetime
name=input("enter you good name: ")
a=int(input("enter you umrr: "))

y = datetime.datetime.now()

if (a==95):
 print("you are already 95 ")

elif (0<a<95):
 print(f"you will be 95 at :{((95-a)+y.year)}")

elif (a<0):
 print("you were not yet born")

elif (a>117):
 print("you have crossed age limit")
