import numpy as np
zeroes_array = np.zeros((3, 4)) # np.zeros(shape)
'''
zeroes_array = np.zeros(3)  for 1D array of length 3
zeroes_array = np.zeros((3, 4)) for 2D array with 3 rows and 4 columns
'''
print("Array of zeroes:\n", zeroes_array)

ones_array = np.ones((2, 5)) # np.ones(shape)
'''
ones_array = np.ones((2, 5)) for 2D array with 2 rows and 5 columns
ones_array = np.ones(2) for 1D array of length 2
'''
print("Array of ones:\n", ones_array)

flled_array = np.full((3, 3), 7) # np.full(shape, fill_value)
'''
flled_array = np.full((3, 3), 7) for 2D array with 3 rows and 3 columns filled with 7
flled_array = np.full(3, 7) for 1D array of length 3 filled with 7
'''
print("Array filled with 7:\n", flled_array)

# creating sequence of numbers
seq_array = np.arange(1,10,2) # np.arange(start, stop, step)
print("Sequence array from 1 to 10 with step 2:\n", seq_array)

# creating identity matrix
identity_matrix = np.eye(4) # np.eye(size)
print("Identity matrix of size 4:\n", identity_matrix)