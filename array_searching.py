# SEARCHING ARRAY 
# you can search an array for a cerwain value, and return the indexes that get a match 
# to search an array, use the where() method

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])

x = np.where(arr == 4)
print(x)

# the example above will return a tuple: (array([3,5,6],)
# which means that the value 4 is present at index 3,5 and 5

arr2 = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr2 %2 == 0)
print(x)

#  find the indexes where the values are odd:

arr3 = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr3%2 == 1)
print(x)

# search sorted
# there is a method called searchsorted() which performs a binary search is the array,
# and returns the index where the specified value would be inserted to maintain the search order

# NOTE : THE searchsorted() method is assumed to be used on sorted arrays.

arr4 = np.array([6,7,8,9])
x = np.searchsorted(arr4,7)
y = np.searchsorted(arr4,7,side = 'right')
print(x)
print(y)


# to search for more than one vlaue, use an array with the specified values

arr5 = np.array([1,3,5,7])
z = np.searchsorted(arr,[2,4,6])

print(z)