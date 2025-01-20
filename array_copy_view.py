# ARRAY COPY VS VIEW 

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

x = arr.copy()
arr[0] = 69

print(arr)
print(x)

x[1] = 96
print(x)


print(x+arr)


arr.sort()
print(arr)

arr

y = arr.view()
print(y)
print(x)

print(type(y))
print(x.base)
print(y.base)

