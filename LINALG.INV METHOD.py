# linalg.inv method

# EXAMPLE A
import numpy as np
from numpy.linalg import inv

A = np.array([[2.5, 3.7], [4.9, 5.1]])

result = inv(A)

print(f'EXAMPLE A:{result}')

# EXAMPLE B
import numpy as np
from numpy.linalg import inv

A = np.array([[1, 2], [3, 4]])

result = inv(A)

print(f'EXAMPLE B:{result}')

# EXAMPLE C
import numpy as np
from numpy.linalg import inv

A = np.array([[2, 3], [1,3]])

result = inv(A)

print(f'EXAMPLE C:{result}')