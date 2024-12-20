import numpy as np
# no of dimensional
# zero dimensional
a=np.array(50)
print(a.ndim)
# one dimensional
b=np.array([40,50])
print(b.ndim)
# four dimensional
c=np.array([[[[1,2,3,4]]]])
print(c.ndim)
# two dimensional
d=np.array([[10,20],[30,40]])
print(d.ndim)
# three dimensional
e=np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
print(e.ndim)

# no of dimensional
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# it is 2 dimensional and it is coming zeros rows (3)and colunms(5)
arr=np.zeros((3,5))
print(arr)

# it
arr1=np.zeros((3,5,6))
print(arr1)

# it is one
arr2=np.ones((3,5,6))
print(arr2)

# it is arrange
x=np.arange(100,2,-5)
print(x)

x=np.arange(0,20,5)
print(x)

x=np.arange(100)
print(x)

arr=np.arange(10)
print(arr)

# it is linespace
x=np.linspace(0,2,9)
print(x)

y=np.linspace(0,10,5)
print(y)

x1=np.linspace(0,10,10,endpoint=True)
print(x1)

x2=np.linspace(0,10,10,endpoint=False)
print(x2)

arr=np.linspace(1,4,6)
print(arr)

arr=np.linspace(1,10,6)
print(arr)