'''
Given a square matrix, calculate the absolute difference between
the sums of its diagonals.
For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal 1 + 5 9 = 15.
The right to left diagonal 3 + 5 + 9 = 17.
Their absolute difference is |15 - 17| = 2.
'''
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    length_row = len(arr[0])
    diag1 = 0
    diag2 = 0
    j = 0
    for i in range(length_row):
        diag1 += arr[i][j]
        diag2 += arr[i][length_row - j - 1]
        j += 1
    # if diag1 > diag2:
    #     return diag1 - diag2
    # else:
    #     return diag2 - diag1
    return abs(diag1 - diag2)


if __name__ == '__main__':
    fptr = open('3_test.txt', 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
