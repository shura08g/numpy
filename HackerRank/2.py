'''
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Print the integer sum of the elements in the array.
'''


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = 0
    for i in ar:
        result += i
    return result


if __name__ == '__main__':
    fptr = open('2_test.txt', 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
