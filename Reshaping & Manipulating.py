import numpy as np
'''
rehaping : 
convert a 1D array to a 2D array without changing data
arr.reshape(rows, cols)
it returns a view of the original array does not create a copy
'''
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)


'''
Flattening :
convert a multi-dimensional array to a 1D array
.ravel() - returns a flattened view of the original array
.flatten() - returns a flattened copy of the original array

'''
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print( arr_2d.ravel()) #[1 2 3 4 5 6] view of original array
print( arr_2d.flatten()) #[1 2 3 4 5 6] copy of original array