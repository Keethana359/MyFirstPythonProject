import math
 # directly use from math import sqrt , print(sqrt(r))
#  using area of circle
r=6
area=math.pi*r*r
print("area of the circle",area)

# using squre
r=256
print(math.sqrt(r))
# using area of circle value
def area_circle(r):
    a=math.pi*r*r
    return a
print("area of circle:",area_circle(5))

# highest number value it is going to next point value
x=5.5
print(math.ceil(x))
# lowest number value it is going to previous value
x=5.5
print(math.floor(x))
# using cos,sin,tan
x=5
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))

# using  x pow of y
x=4
y=5
print(math.pow(x,y))