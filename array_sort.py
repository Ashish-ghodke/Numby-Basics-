# sorting arrays

# sorting means putting elements in an ordered sequence()
# the numpy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

arr = np.array([3,4,5,2,4,1,0])
arr.sort()
print(arr)  # Output: [0 1 2 3 4 4

print(np.sort(arr))

# NOTE: THIS METHOD RETURNS A COPY OF TEH ARRAY, LAVING THE ORIGINAL ARRAY UNCHANGED.

# WE CAN ALSO SORT ARRAYS OF STRINGS, OR ANY OTHER DATA TYPE:

arr2 = np.array(['a','z','s','g','n','k','u'])
print(np.sort(arr2))
arr2.sort()
print(arr2)


# sorting a 2D array
# if we use the sort() method on a 2D array, both array will be sorted:

arr3 = np.array([[1,5,36,6,3,5],[2,7,3,5,1,0]])
print(np.sort(arr3))