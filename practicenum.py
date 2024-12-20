import numpy as np
a=np.array([1,2,3])
print(a)
print(a.ndim)

# zeros
x=np.zeros((3,4))
print(x)

# ones
x=np.ones((2,3,4))
print(x)
# numpy.ndarray it is remove of dots
x=np.ones((2,3,4),dtype=np.int16)
print(x)
print(type(x))

# arange
d=np.arange(10,25,5)
print(d)

# linspace
e=np.linspace(0,2,9)
print(e)

# full type
f=np.full((2,2),7)
print(f)

# eye type
x=np.eye(2)
print(x)

# random type
arr=np.random.random((2,2))
print(arr)

# empty
arr=np.empty((3,2))
print(arr)

# arithmetic opertor
# substract opertor
a=np.array([10,20,30])
b=np.array([5,15,25])
add=a+b
print(add)
print(a-b)
print(a*b)
print(a/b)
# modular 
mod=np.mod(a,b)
print(mod)
# reminder 
rem=np.remainder(a,b)
print(rem)
# power
pow=np.power(a,b)
print(pow)
# sin
sin=np.sin(a)
print(sin)
# cos
cos=np.cos(b)
print(b)
# squre
sqrt=np.sqrt(a)
print(sqrt)
# exp
exp=np.exp(a)
print(exp)
# log
log=np.log(a)
print(a)