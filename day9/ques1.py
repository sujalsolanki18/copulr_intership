import numpy as np

arr=np.array([1,2,3],ndmin=2)
arr2D=np.array([[4,5,6],[10,11,12]])
arr3=np.concatenate((arr,arr2D))
print(arr3)
