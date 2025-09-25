import numpy as np

arr = nparray([1, 2, 3, 4, 5])

# adding 5 to each element
arr_plus_5 = arr + 5
print("Array after adding 5 to each element:", arr_plus_5)

# multiplying each element by 3
arr_times_3 = arr * 3
print("Array after multiplying each element by 3:", arr_times_3)

# squaring each element
arr_squared = arr ** 2
print("Array after squaring each element:", arr_squared)

# aggregate functions
print("sum of all elements:", np.sum(arr)) # sum of all elements
print("mean of all elements:", np.mean(arr)) # mean of all elements
print("maximum element:", np.max(arr)) # maximum element
print("minimum element:", np.min(arr)) # minimum element
print("standard deviation:", np.std(arr)) # standard deviation
print("variance:", np.var(arr)) # variance
