# ===================
# NumPy Cheat Sheet
# Used for numerical computing, handling arrays, and matrix operations.
# ===================

# Importing NumPy
import numpy as np

# ===================
# Creating Arrays
# ===================
arr = np.array([1, 2, 3])  # 1D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
zeros = np.zeros((2, 3))  # Array of zeros
ones = np.ones((3, 2))  # Array of ones
full = np.full((2, 3), 7)  # Array filled with a constant value
arange = np.arange(0, 10, 2)  # Array with values from 0 to 10 with step 2
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1

# ===================
# Basic Operations
# ===================
arr = np.array([1, 2, 3, 4])

# Element-wise operations
arr + 2  # [3, 4, 5, 6]
arr - 2  # [-1, 0, 1, 2]
arr * 2  # [2, 4, 6, 8]
arr / 2  # [0.5, 1.0, 1.5, 2.0]

# Element-wise comparison
arr > 2  # [False, False, True, True]
arr == 2  # [False, True, False, False]

# ===================
# Mathematical Functions
# ===================
arr = np.array([1, 2, 3, 4])

np.sum(arr)  # Sum of array elements
np.prod(arr)  # Product of array elements
np.mean(arr)  # Mean of array elements
np.median(arr)  # Median of array elements
np.std(arr)  # Standard deviation
np.min(arr)  # Minimum value
np.max(arr)  # Maximum value

# ===================
# Array Indexing and Slicing
# ===================
arr = np.array([10, 20, 30, 40, 50])

# Indexing
first_element = arr[0]  # 10
last_element = arr[-1]  # 50

# Slicing
slice1 = arr[1:4]  # [20, 30, 40]
slice2 = arr[:3]  # [10, 20, 30]
slice3 = arr[2:]  # [30, 40, 50]

# Modifying elements
arr[0] = 100  # [100, 20, 30, 40, 50]

# ===================
# Reshaping Arrays
# ===================
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape (Note: new shape must be compatible with the original shape)
reshaped = arr.reshape((3, 2))  # [[1, 2], [3, 4], [5, 6]]

# Transpose
transposed = arr.T  # [[1, 4], [2, 5], [3, 6]]

# ===================
# Stacking Arrays
# ===================
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])

# Vertical stacking
vstacked = np.vstack((arr1, arr2))  # [[1, 2], [3, 4]]

# Horizontal stacking
hstacked = np.hstack((arr1, arr2))  # [1, 2, 3, 4]

# ===================
# Statistical Functions
# ===================
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.mean(arr)  # Mean of all elements
np.mean(arr, axis=0)  # Mean of each column [2.5, 3.5, 4.5]
np.mean(arr, axis=1)  # Mean of each row [2.0, 5.0]

np.std(arr)  # Standard deviation of all elements

# ===================
# Random Numbers
# ===================
rand_arr = np.random.rand(3, 3)  # 3x3 array with random floats between 0 and 1
rand_int = np.random.randint(0, 10, (3, 3))  # 3x3 array with random ints between 0 and 10
rand_norm = np.random.randn(3, 3)  # 3x3 array with random numbers from standard normal distribution

# Setting the random seed
np.random.seed(42)

# ===================
# Saving & Loading Arrays
# ===================
arr = np.array([1, 2, 3])

# Save array to file
np.save('array.npy', arr)

# Load array from file
loaded_arr = np.load('array.npy')

# Save to text file
np.savetxt('array.txt', arr)

# Load from text file
loaded_txt_arr = np.loadtxt('array.txt')

# ===================
# Useful Tips & Shortcuts
# ===================
# Create identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix

# Create a diagonal matrix
diagonal_matrix = np.diag([1, 2, 3])  # Diagonal matrix with 1, 2, 3 on the diagonal

# Repeat array
repeated_arr = np.tile([1, 2], 3)  # [1, 2, 1, 2, 1, 2]

# Flatten array
flattened = arr.flatten()  # Convert multi-dimensional array to 1D

# ===================
# Broadcasting
# ===================
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Add a scalar to every element
arr + 1  # [[2, 3, 4], [5, 6, 7]]

# Add a 1D array to a 2D array
arr + np.array([1, 0, -1])  # [[2, 2, 2], [5, 5, 5]]

# ===================
# Logical Operations
# ===================
arr = np.array([1, 2, 3, 4])

np.all(arr > 0)  # True if all elements are > 0
np.any(arr > 2)  # True if any element is > 2

# Conditional element selection
np.where(arr > 2, arr, -1)  # Elements > 2 stay, others become -1

# ===================
# End of Cheat Sheet
# ===================