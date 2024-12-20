# zero dimensional method
import numpy 
arr=numpy.array(10)
print(arr)

# one dimensional method
# referring name as same things
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# stored under version attribute
print(np.array([1,2,3,4,5]))
# this is type of array
# numpy.ndarray
print(type(arr))

# two dimensional method
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
# create 2d array containing two array value 123 and 456
print(np.array([[10,20],[30,40]]))
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr1)
print(arr)

# three dimensional value
# create 3d array with 2d array ,both containing 2d array 123 and 456
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

# check no of dimensional(ndim)
a=np.array(10)
b=np.array([10,20])
c=np.array([[10,20],[30,40]])
d=np.array([[[10,20],[30,40]],[[50,60],[70,80]]])

# zero dimensional
print(a.ndim)
# one dimensional
print(b.ndim)
# two dimensional
print(c.ndim)
# three dimensional
print(d.ndim)


# aaccess elemem=nt
arr=np.array([1,2,3,4])
arr[0]
print(arr[0])
print(arr[1]+arr[2])
print(arr[1]-arr[2])
print(arr[1]*arr[2])
print(arr[1]/arr[2])

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

# it is linespace
x=np.linspace(0,2,9)
print(x)

y=np.linspace(0,10,5)
print(y)

x1=np.linspace(0,10,10,endpoint=True)
print(x1)

x2=np.linspace(0,10,10,endpoint=False)
print(x2)