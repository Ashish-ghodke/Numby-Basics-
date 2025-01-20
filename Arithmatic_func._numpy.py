# ARITHMATIC FUNCTION AND OPERATION IN NUMPY 
# np.min()
# np.max()
# np.argmin()
# np.sqrt()
# np.sin()
# np.cos()
# np.cumsum()

import numpy as np          

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

print("min:", np.min(arr))
print("max:", np.max(arr))
print("argmin:", np.argmin(arr))
print("sqrt:", np.sqrt(arr))
print("mean:",np.mean(arr))
print("median:",np.median(arr))


arr2 = [[1,2,3,4],[5,6,7,8]]
print(arr2)
print("min : ",np.min(arr2))
print(np.min(arr2,axis=1))
print("sqrt",np.sqrt(arr2))

print("cumsum : ", np.cumsum(arr2))

