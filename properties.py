# to find the shape of an array
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3.04],
                     [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])

print("Shape of the array:", array_2d.shape) # Output: (2, 3) 2 rows, 3 columns
print("Shape of 3D array:", array_3d.shape) # Output: (2, 2, 2) 2 blocks, each with 2 rows and 2 columns

# to check the size of an array
print("Size of the array:", array_2d.size) # Output: 6 (total number of elements)
print("Size of 3D array:", array_3d.size) # Output: 8 (2*2*2 = 8 elements)

# to find the number of dimensions of an array
print("Number of dimensions:", array_2d.ndim) # Output: 2 (2D array) ndim = number of dimensions
print("Number of dimensions of 3D array:", array_3d.ndim) # Output: 3 (3D array)

# to find the data type of elements in an array
print("Data type of elements:", array_2d.dtype) # Output: float64 (since one element is float)
print("Data type of elements in 3D array:", array_3d.dtype) # Output: int64 

# to change the data type of elements in an array
array_float = array_1d.astype(float) # astype(new_type)
print("Array with float data type:", array_float)
print("Data type after conversion:", array_float.dtype) # Output: float64