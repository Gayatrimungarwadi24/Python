import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print("Array is of type: ",type(arr))
print("No. of dimensions: ",arr.ndim)
print("Shape of array: ",arr.shape)
print("Size of array: ",arr.size)
print("Array stores elements of type: ",arr.dtype)

arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr=arr2.reshape(4,3)
print(new_arr)