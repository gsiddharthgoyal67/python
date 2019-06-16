#!usr/bin/python3
 
import datetime

now=datetime.datetime.now()

gender=input("what is your gender :(M/F)")
gen=" "
if gender == "M":
	gen="Sir"
else : 
	gen="Ma'am"

name=input(f"enter your good name ,{gen}: ")
print("current date and time :")
print(now)
print(now.strftime("%d-%m-%Y %H:%M:%S"))



if now.hour>=0 and now.hour<12:
 print(f"good morning {gen}")

elif now.hour>=12 and now.hour<16:
 print(f"good afternoon  {gen}")

elif now.hour>=16 and now.hour<19:
 print(f"good evening  {gen}")

elif now.hour>=19 and now.hour<0:
 print(f"good night  {gen}")

