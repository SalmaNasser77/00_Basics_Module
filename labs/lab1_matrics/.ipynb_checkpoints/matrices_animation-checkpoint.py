import numpy as np

##creating a matrix with a certain size:##

# Define a 3x3 matrix filled with zeros and specifying the datatype
matrix = np.zeros((3, 3), dtype=int)
print(matrix)

# Define a 4x5 matrix filled with ones
matrix = np.ones((4, 5))
print(matrix)

# Define a 2x2 matrix filled with 7
matrix = np.full((2, 2), 7)
print(matrix)


# Define a 4x4 identity matrix
matrix = np.identity(4)
print(matrix)
