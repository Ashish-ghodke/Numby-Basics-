# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
# Example
# Check how many dimensions the arrays have:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f" {a} \n a is the {a.ndim}D array \n")
print(f" {b} \n b is the {b.ndim}D array \n")
print(f" {c} \n c is the {c.ndim}D array \n")
print(f" {d} \n dis the {d.ndim}D array \n")

