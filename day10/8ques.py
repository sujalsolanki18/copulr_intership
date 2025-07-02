import numpy as np
arr1=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr2=np.array([9,-6,17])
res3=np.linalg.solve(arr1,arr2)
print("solution of algebra is ",res3)
