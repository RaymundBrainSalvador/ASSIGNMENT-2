# FLATTEN METHOD

# EXAMPLE A
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

result = arr.flatten()
print(f'EXAMPLE A:{result}')

# EXAMPLE B
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

result = arr.flatten()
print(f'EXAMPLE B:{result}')

# EXAMPLE C
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)

result= C.flatten()
print(f'EXAMPLE C:{result}')