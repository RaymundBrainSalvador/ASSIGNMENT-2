# linalg.det method

# EXAMPLE A
import numpy as np
from numpy.linalg import det

# Define a matrix
A = np.array([[1, 2], [3, 4]])

result = det(A)

print(f'EXAMPLE A:{result}')

# EXAMPLE B
import numpy as np
from numpy.linalg import det

A = np.array([[2, 3], [4, 5]])

result = det(A)
print(f'EXAMPLE B:{result}')

# EXAMPLE C
import numpy as np
from numpy.linalg import det

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

result = det(A)
print(f'EXAMPLE C:{result}')