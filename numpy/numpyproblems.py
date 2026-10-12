import numpy as np


# ============================================================
# 1. One-dimensional array: display array, size, data type,
#    and number of dimensions
# ============================================================

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


# ============================================================
# 2. Arithmetic operations on two NumPy arrays
# ============================================================

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 5, 8, 10])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)


# ============================================================
# 3. Maximum, minimum, sum and average
# ============================================================

arr = np.array([10, 25, 15, 40, 30, 5, 60, 45, 20, 35])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# ============================================================
# 4. Boolean indexing: separate even and odd numbers
# ============================================================

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Original Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# ============================================================
# 5. Reshape 1 to 12 into 2x6, 3x4 and 4x3 matrices
# ============================================================

arr = np.arange(1, 13)

print("Original Array:")
print(arr)

matrix_2x6 = arr.reshape(2, 6)
matrix_3x4 = arr.reshape(3, 4)
matrix_4x3 = arr.reshape(4, 3)

print("\n2 x 6 Matrix:")
print(matrix_2x6)

print("\n3 x 4 Matrix:")
print(matrix_3x4)

print("\n4 x 3 Matrix:")
print(matrix_4x3)


# ============================================================
# 6. Addition of two 3x3 matrices
# ============================================================

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(result)


# ============================================================
# 7. Matrix multiplication
# ============================================================

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

result = np.matmul(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication:")
print(result)


# ============================================================
# 8. Transpose of a 3x4 matrix
# ============================================================

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)


# ============================================================
# 9. Access elements of a 4x4 matrix
# ============================================================

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nLast Column:")
print(matrix[:, -1])

print("\nDiagonal Elements:")
print(np.diag(matrix))

print("\nSecond and Third Rows:")
print(matrix[1:3])


# ============================================================
# 10. Sum of each row and each column
# ============================================================

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)

print("\nSum of Each Row:")
print(row_sum)

print("\nSum of Each Column:")
print(column_sum)


# ============================================================
# 11. Slicing an array from 1 to 20
# ============================================================

arr = np.arange(1, 21)

print("Original Array:")
print(arr)

print("\nFirst 5 Elements:")
print(arr[:5])

print("\nLast 5 Elements:")
print(arr[-5:])

print("\nAlternate Elements:")
print(arr[::2])

print("\nReverse Order:")
print(arr[::-1])


# ============================================================
# 12. Replace elements greater than 50 with 0
# ============================================================

arr = np.array([10, 25, 60, 45, 75, 30, 90, 55, 40, 80])

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("\nAfter Replacing Values Greater Than 50 With 0:")
print(arr)


# ============================================================
# 13. Sort array in ascending and descending order
# ============================================================

arr = np.array([50, 10, 40, 20, 80, 30, 70, 60])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original Array:")
print(arr)

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)


# ============================================================
# 14. Find unique elements
# ============================================================

arr = np.array([10, 20, 10, 30, 20, 40, 50, 30, 60, 50])

unique_elements = np.unique(arr)

print("Original Array:")
print(arr)

print("\nUnique Elements:")
print(unique_elements)


# ============================================================
# 15. Horizontal and vertical concatenation
# ============================================================

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

horizontal = np.hstack((arr1, arr2))
vertical = np.vstack((arr1, arr2))

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nHorizontal Concatenation:")
print(horizontal)

print("\nVertical Concatenation:")
print(vertical)


# ============================================================
# 16. Marks of 10 students
#     Highest, lowest, average, median, standard deviation
# ============================================================

marks = np.array([85, 72, 90, 65, 78, 88, 92, 70, 80, 95])

print("Marks:", marks)

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# ============================================================
# 17. Marks of 20 students
#     Display students scoring above average
# ============================================================

marks = np.array([
    75, 82, 68, 90, 55,
    88, 92, 70, 85, 78,
    60, 95, 72, 81, 67,
    89, 76, 94, 58, 83
])

average = np.mean(marks)

above_average = marks[marks > average]

print("Marks:")
print(marks)

print("\nClass Average:", average)

print("\nMarks Above Average:")
print(above_average)


# ============================================================
# 18. Create a 3D array of shape (2, 3, 4)
# ============================================================

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nNumber of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# ============================================================
# 19. Access elements from a 3D array
# ============================================================

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nFirst Element:")
print(arr[0, 0, 0])

print("\nLast Element:")
print(arr[-1, -1, -1])

print("\nElement at index [0,1,2]:")
print(arr[0, 1, 2])

print("\nElement at index [1,2,3]:")
print(arr[1, 2, 3])


# ============================================================
# 20. Sum of 3D array
#     Sum of all elements
#     Sum of each layer
#     Sum along rows
#     Sum along columns
# ============================================================

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nSum of All Elements:")
print(np.sum(arr))

# Sum of each 3x4 layer
print("\nSum of Each Layer:")
print(np.sum(arr, axis=(1, 2)))

# Sum along rows
print("\nSum Along Rows:")
print(np.sum(arr, axis=2))

# Sum along columns
print("\nSum Along Columns:")
print(np.sum(arr, axis=1))


# ============================================================
# 21. Random 3D array and replace values greater than 50
# ============================================================

np.random.seed(1)

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("\nAfter Replacing Values Greater Than 50 With 0:")
print(arr)


# ============================================================
# 22. Random 3D array of shape (3,4,5)
#     Mean, median, standard deviation, variance,
#     minimum and maximum
# ============================================================

np.random.seed(2)

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D Array:")
print(arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# ============================================================
# 23. Flatten a 3D array
# ============================================================

arr = np.arange(1, 25).reshape(2, 3, 4)

flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)


# ============================================================
# 24. Flatten 1 to 27 and calculate statistics
# ============================================================

arr = np.arange(1, 28).reshape(3, 3, 3)

flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

print("\nSum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))


# ============================================================
# 25. Random 3D array, flatten and filter elements
#     Greater than 50
#     Even numbers
#     Less than average
# ============================================================

np.random.seed(3)

arr = np.random.randint(1, 101, size=(3, 4, 5))

flattened = arr.flatten()

average = np.mean(flattened)

greater_than_50 = flattened[flattened > 50]
even_numbers = flattened[flattened % 2 == 0]
less_than_average = flattened[flattened < average]

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

print("\nElements Greater Than 50:")
print(greater_than_50)

print("\nEven Numbers:")
print(even_numbers)

print("\nAverage:", average)

print("\nElements Less Than Average:")
print(less_than_average)