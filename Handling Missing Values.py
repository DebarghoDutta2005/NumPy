'''
np.isnan(array) function is used to detect missing values in a NumPy array.
np.nan_to_num() function is used to convert NaN values to a specified number.
np.isinfinite() function is used to check for finite values (not NaN or infinite) in a NumPy array.
NaN = Not a Number, boolean = True/False
'''
import numpy as np
arr = np.array([1, 2, np.nan, 4, 5, np.nan])

print(np.isnan(arr))  # flase, false, true, false, false, true

print(np.nan_to_num(arr, nan=-1))  # [ 1.  2. -1.  4.  5. -1.]
arr1 = np.array([1, 2, np.inf, 4, 5, np.nan, -np.inf])
print(np.isfinite(arr1))  # [ True  True False  True  True False False]
print(np.nan_to_num(arr1, nan=-1, posinf=100, neginf=-100))  # [   1.    2.  100.    4.    5.   -1. -100.]