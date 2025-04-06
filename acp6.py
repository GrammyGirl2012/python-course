import numpy as np

# Create two NumPy arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("Array a:", a)
print("Array b:", b)

# Addition
add = a + b
print("Addition:", add)

# Subtraction
sub = a - b
print("Subtraction:", sub)

# Multiplication (element-wise)
mul = a * b
print("Multiplication:", mul)

# Division (element-wise)
div = a / b
print("Division:", div)

# Some useful NumPy operations
print("Mean of a:", np.mean(a))
print("Max of b:", np.max(b))
print("Dot product of a and b:", np.dot(a, b))
print("Square root of a:", np.sqrt(a))
print("Reshaped a (2x2):\n", a.reshape(2, 2))

