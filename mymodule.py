#!usr/bin/python3
 
import datetime

now=datetime.datetime.now()

name=input(f"enter your good name: ")
print("current date and time :")
print(now)
print(now.strftime("%d-%m-%Y %H:%M:%S"))



if now.hour>=0 and now.hour<12:
 print(f"good morning ")

elif now.hour>=12 and now.hour<16:
 print(f"good afternoon ")

elif now.hour>=16 and now.hour<19:
 print(f"good evening  ")

elif now.hour>=19 and now.hour<0:
 print(f"good night  ")



def add(x,y):
 print(x+y)

