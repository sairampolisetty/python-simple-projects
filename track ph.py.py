from pickle import TRUE
from time import time
from numpy import number
import phonenumbers
from phonenumbers import carrier,timezone,geocoder

number=input("enter yout number")
#number=+919666988423
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,'en')
reg=geocoder.description_for_number(phone,'en')
valid=phonenumbers.is_valid_number(phone)
if valid==1:
    print('yes its valid number')
else:
    print('its not a valid number')
    exit()
#print(valid)
print(time)
print(car)
print(reg)
print(phone)