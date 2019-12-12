import numpy as np

# a = np.array([1, 2, 3])  # int32
a = np.array([1, 2, 3], dtype='int16')
print(f'Array a: {a}')

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(f'Array b: {b}')

# Get Dimension
print(f'Dimension a: {a.ndim}')  # 1
print(f'Dimension b: {b.ndim}')  # 2

# Get Shape
print(f'Shape a: {a.shape}')  # (3,)
print(f'Shape b: {b.shape}')  # (2, 3)

# Get Type
print(f'Type a: {a.dtype}')  # int16
print(f'Type b: {b.dtype}')  # float64

# Get Size
print(f'Size a: {a.size}')  # 3
print(f'Size b: {b.size}')  # 6

# Get Size item
print(f'Size item a: {a.itemsize}')  # 2
print(f'Size item b: {b.itemsize}')  # 8

# Get total size
print(f'Total size a: {a.size * a.itemsize}')  # 6
print(f'Total size b: {b.size * b.itemsize}')  # 48

# Get total size in bytes
print(f'Size in bytes a: {a.nbytes}')  # 6
print(f'Size in bytes b: {b.nbytes}')  # 48

# Accesing/Changing specific elements, row, colums, ect.
a2 = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a2)

# Get a specific element [r, c]
print(a2[1, 5])  # 13
print(a2[1, 2::2])  # [10 12 14]

# Get a specific column
print(a2[:, 0])  # [1 8]
print(a2[:, :2])  # [[1 2]
                  #  [8 9]]

a2[1, 5] = 99
a2[:, 2] = [55, 77]
print(a2)  # [[ 1  2 55  4  5  6  7]
           #  [ 8  9 77 11 12 99 14]] 

d3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(d3)  # [[[1 2]
           #   [3 4]]
           #  [[5 6]
           #   [7 8]]]
print(d3.ndim)  # 3       
print(d3.shape)  # (2, 2, 2)
print(d3[0, 1, 1])  # 4
print(d3[1][1][0])  # 7


#Initializing different types of array
zero_array = np.zeros((3, 3), dtype=int)
print(zero_array)  # [[0 0 0]
                   #  [0 0 0]
                   #  [0 0 0]]

ones_array = np.ones((3, 3), dtype=int)
print(ones_array)  # [[1 1 1]
                   #  [1 1 1]
                   #  [1 1 1]]

num_array = np.full((2, 2), 5)
print(num_array)  # [[5 5]
                  #  [5 5]]

fill_array = np.full_like(num_array, 7)
print(fill_array) # [[7 7]
                  #  [7 7]]

fill_array2 = np.full(num_array.shape, 9)
print(fill_array2) # [[9 9]
                  #   [9 9]


# Random decimal numbers
rand_arr = np.random.rand(4, 2)
print(rand_arr)

rand_arr2 = np.random.random_sample(b.shape)
print(rand_arr2)

# Random integer numbers
randint_arr = np.random.randint(-10, 10, size=(3, 3))
print(randint_arr)

# The identy matrix
matrix_arr = np.identity(5)
print(matrix_arr)

r1 = np.repeat(a, 3, axis=0)
print(r1)  # [1 1 1 2 2 2 3 3 3]


# Mathematics
a += 2
print(a)  # [3 4 5]

a -= 2
print(a)  # [1 2 3]

a *= 3
print(a)  # [3 6 9]

a //= 3
print(a)  # [1 2 3]

a = a / 1
print(a)  # [1. 2. 3.]

print(np.cos(a))  # [ 0.54030231 -0.41614684 -0.9899925 ]
print(np.sin(a))  # [0.84147098 0.90929743 0.14112001]
print(np.tan(a))  # [ 1.55740772 -2.18503986 -0.14254654]


# Linear Algebra
a_arr = np.ones((2, 3))
print(a_arr)
b_arr = np.full((3, 2), 2)
print(b_arr)
c_arr = np.matmul(a_arr, b_arr)
print(c_arr)  # [[6. 6.]
              #  [6. 6.]]

# Find determimamt
print(np.linalg.det(c_arr))  # 0.0


# Statistics
print(np.min(a2))  # 1
print(np.max(a2))  # 99
print(np.max(a2, axis=1))  # [55 99]
print(np.sum(a2))  # 310
print(np.sum(a2, axis=0))  # [  9  11 132  15  17 105  21]


# Reorgonizing arrays
before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(before.shape)  # (2, 4)
after = before.reshape(4, 2)
print(after.shape)  # (4, 2)
print(after)


#  Vertically stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

v3 = np.vstack([v1, v2, v1, v2])
print(v3)  # [[1 2 3 4]
           #  [5 6 7 8]
           #  [1 2 3 4]
           #  [5 6 7 8]]

# Horizontal stack
v4 = np.hstack(v3)
print(v4)  # [1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8]


# Miscellaneous

# Load data from file
filedata = np.genfromtxt('np_arr_test.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean masking and Advanced indexing
print(filedata > 50)
print(filedata[filedata > 50])  # [87 89 55 54 87]
print(np.any(filedata > 50, axis=0))  # [False False  True False  True  True False  True]
print(np.all(filedata > 50, axis=0))  # [False False  True False  True  True False  True]
