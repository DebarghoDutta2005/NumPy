import numpy as np

'''
np.insert(arr, index, value, axis=None)
Insert values into an array at specified indices along a given axis.
array - original array
axis - axis along which to insert (None for flattened array)
axis = 0, row-wise insertion
axis = 1, column-wise insertion
'''
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.insert(arr, 2, 25) #insert 25 at index 2
print(new_arr) #[10 20 25 30 40 50]

arr_2d = np.array([[1, 2, 3], [7, 8, 9]])
new_arr_2d = np.insert(arr_2d, 1, [4,5,6], axis=0) #insert row at index 1
print(new_arr_2d)
#new_arr_2d = np.insert(arr_2d, 1, [4,5,6], axis=1) #insert column at index 1

'''
Appending
np.append(arr, values, axis=None)
'''
arr = np.array([10, 20, 30])
appended_arr = np.append(arr, [40, 50]) #append values to the end
print(appended_arr) #[10 20 30 40 50]

'''
concatenation
np.concatenate((arr1, arr2, ...), axis=0)
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2)) #concatenate along axis 0
print(concatenated_arr) #[1 2 3 4 5 6]

'''
removing elements
np.delete(arr, index, axis=None)
'''
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 2) #remove element at index 2
print(new_arr) #[10 20 40 50]

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr_2d = np.delete(arr_2d, 1, axis=0) #remove row at index 1
print(new_arr_2d)