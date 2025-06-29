import numpy as np

 #Create a NumPy array with random values (4x2)
random_array = np.random.rand(4, 2)
print(random_array)

#Create an empty NumPy array (4x2)
empty_array = np.empty((4, 2))
print(empty_array)


zeros_array = np.zeros((3, 5))
print("\n3x5 array filled with zeros:")
print(zeros_array)

# Np array (4x3x2) filled with all ones
ones_array = np.ones((4, 3, 2))
print("\n4x3x2 array filled with ones:")
print(ones_array)
