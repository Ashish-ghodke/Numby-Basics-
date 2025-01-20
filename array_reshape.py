# Reshape Array

import numpy as np 

arr = np.array([0,1,2,3,4,5,6,7,8,9])

newarr = arr.reshape(2,5)
print(newarr)
newarr = arr.reshape(5,2)
print(newarr)

print(arr.reshape(2,5).base)

arr = np.array([1,2,3,4,5,6,7,8])


newarr = arr.reshape(2,2,-1)
print(newarr)