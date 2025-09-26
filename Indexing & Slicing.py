import numpy as np
'''
Indexing
array[index] #1D array indexing
array[row_index, col_index] #2D array indexing
'''

arr = np.array([10, 20, 30, 40, 50])
print(arr[0]) #10
print(arr[2]) #30
print(arr[-1]) #50
print(arr[10]) #IndexError: index 10 is out of bounds for axis 0 with size 5

'''
slicing[start:stop:step] 
start - starting index (inclusive)
stop - ending index (exclusive) 
step - step size (default is 1)

arr[start:stop] , start to stop-1
'''

arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4]) #[20 30 40]
print(arr[:3]) #[10 20 30]
print(arr[2:]) #[30 40 50]
print(arr[::2]) #[10 30 50] pick every second element
print(arr[::-1]) #[50 40 30 20 10] reverse the array


'''
Fancy Indexing
select multiple elements using an array of indices
'''
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]]) #[10 30 50] copy of the original array

'''
filtering
use boolean arrays to filter elements
'''
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25]) #[30 40 50] elements greater than 25
print(arr[(arr > 15) & (arr < 45)]) #[20 30 40] elements between 15 and 45