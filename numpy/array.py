import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(arr[0])
print(arr[2])
print(type(arr))

# 2D array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print("2nd element of 1st row: ",arr1[0,1])
print("2nd element of 2st row: ",arr1[1,1])

# 3D array
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
print(arr2[0,0,2])
print(arr2[1,1,2])