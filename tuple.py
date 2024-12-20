# import math
# # directly use from math import sqrt , print(sqrt(r))
# r=6
# area=math.pi*r*r;
# print("area of the circle",area)
# r=256
# print(math.sqrt(r))
from os import add_dll_directory

x=(1,2,3,4,5)
print(x)

# tuple cannot be modify.we are immutable we cannot add,update,delete item of tuple
cars=('tesla','bmw','honda','ford')
print(cars[1])
# cars[2]= 'adi' error

# using length of present of item in tuple
cars=('tesla','bmw','honda','ford')
print("total length :",len(cars))

#using for loop in tuple
cars=('tesla','bmw','honda','ford')
for x in cars:
    print(x)

# using exist item in  tuple  boolen reult
cars=('tesla','bmw','honda','ford')
print('alto' in cars)
print('ford'in cars)


