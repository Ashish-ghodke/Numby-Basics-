# NUMPY SPLITTING ARRAY


# SPLITTING NUMPY ARRYS 
# splitting is reverse operation of joining
# joining merges multiple arrays into one and splitting breaks one array into multiple.
# we use array_split() for splitting arrays, we pass it the array we wnt to split and the number of splits.

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])

newarr = np.array_split(arr,4)
print(newarr)
print(len(newarr))
a = newarr.copy()
print(a)
print(type(newarr))

# NOTE the return value is a list containing 4 arrays
# if the array has less elements than required , it will adjust from the end accordingly

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)

print(newarr)

# NOTE : we also have the method split() available but it will not adjust the elements when element are less
#        in sourse array for splitting like in example above, array_split() worked properly but split() would fail.


# split into arrays 
# the return value of the array_split() method is an array containing each of the sp;ot as an array
# if you split an array into 3 arrays, you can access them from the result just like any array element

arr = np.array([1,2,3,4,5,6,7,8])
newarr = np.array_split(arr,4)
print(newarr[0]) # access the first split array
print(newarr[1]) # access the second split array
print(newarr[2]) # access the third split array
print(newarr[3]) # access the fourth split array


# SPLITTING 2D ARRAYS 
# use the same syntax when splitting 2D arrays
# use the array_split() method, pass in the array you want to split and the number of splits you want to do.

arr = np.array([[1,2,3,4],[5,6,7,8]])
newarr = np.array_split(arr,2)
print(newarr) # split the array into 2 arrays
print(newarr[0]) # access the first split array
print(newarr[1]) # access the second split array


arr2 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print(arr.ndim)

newarr2 = np.array_split(arr2,3)
print(newarr2) # split the array into 3 arrays

# the example above return three 2-D arrays.
# example 2

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

newarr3 = np.array_split(arr3,4)
print(newarr3)


arr4 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])

newarr4 = np.array_split(arr4,3, axis=1)
print(newarr4)

# alternate solution hsplit() opposite of hstack()
print()
newarray = np.hsplit(arr4,3)
print(newarray)

# NOTE: similar alternates to vstack() and dstack() are available vsplit() and dsplit()

