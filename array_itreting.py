# Numpy Array Iterating

import numpy as np

arr1 = np.array([1,2,3,4,5])
print("this array is : ",arr1.ndim,"D array")
for x in arr1:
    print(x) # prints each element of the array
    
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(f"this array is : {arr2.ndim} D array")

for x in arr2:
    for i in x:
        print(i)
        

arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(f"this array is : {arr3.ndim} D array")

for x in arr3:
    print(x)
    for i in x:
        print(i)
        for j in i:
            print(j)
            
        
arr4 = np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]])
print(f"this array is : {arr4.ndim} D array")

for x in np.nditer(arr4):
    print(x)
    

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

for x in np.nditer(arr, flags = ['buffered'],op_dtypes=['S']):
    print(x)
    
arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr[:,::2]):
    print(x)

 
arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(arr.ndim)
for idx, x in np.ndenumerate(arr):
    print(idx,x)