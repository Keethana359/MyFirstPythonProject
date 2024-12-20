import numpy as np
#access array element index tyype
x=np.array([1,2,3,])
print(x[0])

arr=np.array([1,2,3,4])
arr[0]
print(arr[0])
# operational method array element
print(arr[1]+arr[2])
print(arr[1]-arr[2])
print(arr[1]*arr[2])
print(arr[1]/arr[2])

# access 2d array element
arr=np.array([[10,20,30],[40,50,60]])
print('3rd element on 1st row:',arr[0,2])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('5th element on 1st row:',arr[1,4])

# access 3d array element
arr=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print('5th element on 1d of on 1st row:',arr[1,1,4])

# 3d array  element
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])

# negative indexing element

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('5th element on 1st row:',arr[1,-1])

# array slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:6])
print(arr[1:])
print(arr[:4])
# negative slicing
print(arr[-4:-1])
# step to jump
print(arr[1:5:2])
print(arr[::3])
# slicind 2d array step
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:5])
print(arr[0:3,3])
print(arr[0:2,0:4])