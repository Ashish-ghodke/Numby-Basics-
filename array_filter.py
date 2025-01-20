# FILTERING ARRAYS
# getting some elements out of an existing array and creating a new array out of then is called filtering

# NOTE: A boolean index list is a list of booeans corresponding to indexes in the array.
# if the value at an index is True, that elemnts is contained in the filtered array, if the value 
# at that index is false that element is excluded from the fitered array.

import numpy as np                  

arr = np.array([41,42,43,44])

x = [True,False,True,False]

newarr = arr[x]
print(newarr)

# CREATING THE FILTER ARRAY 
# in the example above we hard-coded the True and False values, but the common use is to create
# a filter array based on conditions.


# create a filter array that will return only values higher than 42

arr = np.array([41,42,43,44])

# create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, add True to filter_arr, otherwise add False
    if element >= 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


print()
print()
print()

# create a filter array that will return only even elements from the original array:

arr = np.array([1,2,3,4,5,6,7])

# create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is completely divisible by 2, set the value to True , otherwise false
    if element % 2== 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print()
print()
print()


# CREATING FILTER DIRECTLY FROM ARRAY

arr = np.array([41,42,43,44])

filter_arr = arr> 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


print()
print()
print()

# CREATE A FILTER THAT WILL RETURN ONLY EVEN ELEMENTS FORM THE ORIGINAL ARRAY

arr = np.array([1,2,3,4,5,6,7,8])
filter_arr = arr%2 == 0

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)