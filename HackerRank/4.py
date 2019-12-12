'''
Given an array of integers, calculate the fractions of its
elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.

Function Description

Complete the plusMinus function in the editor below.
It should print out the ratio of positive, negative and zero
items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):
    arr: an array of integers

Input Format

The first line contains an integer, n , denoting the size of the array.
The second line contains n space-separated integers describing
an array of numbers

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array
compared to its size.
A decimal representing of the fraction of negative numbers in the array
compared to its size.
A decimal representing of the fraction of zeros in the array compared to
its size.

'''


# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    plus = 0
    minus = 0
    zero = 0
    for i in range(length):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1
    print('%1.6f' % (plus / length))
    print('%1.6f' % (minus / length))
    print('%1.6f' % (zero / length))


if __name__ == '__main__':
    # n = int(input())
    n = 6

    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
