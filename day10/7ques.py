import numpy as np

arr3=np.array([[1, 2, 3],
                 [4, 5, 6]])

arr4=np.array([[6, 5, 4],
                 [3, 2, 1]])

combined=np.concatenate((arr3, arr4))

average = np.mean(combined)
print(average)

median = np.median(combined)
print(f"Median: {median}")

#mode=np.mod(combined)
#print(mode)


