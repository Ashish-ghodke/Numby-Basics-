# Array join
# Joining means putting contents of two or more arrays in a single array.
# We can also use the join() function to join two arrays.
# we pass a sequence of arrays that we want to join to the concattenate() function, along with the axis. 
# if axis is not explicityly passed, it is taken as 0

import numpy as np 

arr1 = np.array([1,2,3,4])
print(f"array 1 is {arr1} ")

arr2 = np.array([5,6,7,8])
print(f"array 2 is {arr2} ")

arrjoin = np.concatenate((arr1,arr2))

print(f"array after join : {arrjoin}")

print(len(arr1))
print(len(arr2))
print(len(arrjoin))

arr1[1] = 42
print(arr1)
print(f"array after change : {arrjoin} ")

# array join using stack functions
# staking is smae as concatenation, the only difference is that stacking is donw along a new axis.
# we pass a sequenceof arrays that we want to join to the stack() method along with the axis. if axis is not explicitly passed, it is taken as 0.

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

newarr = np.stack((arr1, arr2), axis=1)
print(f"array join using stack function: {newarr}")


# stacking alogh rows
# numpy provides a helper function: hstack() to stack along rows

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

stackrowarr = np.hstack((arr1,arr2))

print(f"stack row array : \n{stackrowarr}")

# stacking along columns 
# numpy provides a helper function: vstack() to stack along columns

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

column_stack = np.vstack((arr1,arr2))
print(f"coumn stack array :\n {column_stack}")


# stacking along height (depth)
# numpy provides a helper function: dstack()  to stack along height, which is the same as depth.

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

depth_arr = np.dstack((arr1,arr2))
print(f"depth array :\n {depth_arr}")



arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
