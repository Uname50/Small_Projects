import sys
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([0, .5, 1, 1.5, 2])

# multi-dimensional array
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# show the shape of the array
print(A.shape)

# show the size of the array
print(A.size)

matrix = np.array([
    [1, 2, 3], # 0th dimension
    [4, 5, 6], # 1st dimension
    [7, 8, 9]  # 2nd dimension
])

# access elements of a matrix
matrix[1][0] # -> 1st dimension, 0th element: 4 

matrix[:, :2] # slicing works same as Python 

# replace a row
matrix[1] = np.array([10, 11, 12])

# replacement can be specified once, and NumPy will fill all available spaces with it
matrix[2] = 99