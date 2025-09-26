import numpy as np
'''
vstack() - stack arrays vertically (row-wise)
hstack() - stack arrays horizontally (column-wise)
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
vstacked_arr = np.vstack((arr1, arr2))
print(vstacked_arr)
hasattred_arr = np.hstack((arr1, arr2))
print(hasattred_arr)

'''
np.split() - split an array into multiple sub-arrays
hsplit() - split an array into multiple sub-arrays horizontally (column-wise)
vsplit() - split an array into multiple sub-arrays vertically (row-wise)
'''

arr = np.array([1, 2, 3, 4, 5, 6])
array_split_arr = np.split(arr, 3)
print(array_split_arr)
hsplit_arr = np.hsplit(arr, 3)
print(hsplit_arr)
