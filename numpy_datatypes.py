import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array(["a", "b", "c", "d" ,"e"])
c = np.array([1.0, 2.0, 3.0, 4.0])
d = np.array([True,False])
e = np.array([1.0 + 2.0j, 1.5 + 2.5j])

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d.dtype)
print(e.dtype)

arr1 = np.array([1,2,3,4,5], dtype='U')
arr3 = np.array([1,2,3,4,5], dtype='S')
arr4 = np.array([1,2,3,4,5], dtype='i')
arr5 = np.array([1,2,3,4,5], dtype='F')


print(arr1)
print(arr3)
print(arr4)
print(arr5)

print(arr1.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)

arr = np.array([1,2,3,4,5], dtype='i4')
print(arr)
print(arr.dtype)

x = np.array([1,2,3,4,5])

print(x.dtype)
z = x.astype('i')
print(z.dtype)

y = np.array([1.1,2.1,3.1])

q = arr.astype(int)

print(y.dtype)
print(q.dtype)

# i: Integer
# b: Boolean
# u: Unsigned integer
# f: Float
# c: Complex float
# m: Timedelta
# M: Datetime
# O: Object
# S: String
# U: Unicode string
# V: Fixed chunk of memory for other type

