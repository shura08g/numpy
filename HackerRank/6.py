'''
Given five positive integers, find the minimum and maximum
values that can be calculated by summing exactly four of the
five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.

Input Format
A single line of five space-separated integers.

Output Format
Print two space-separated long integers denoting the respective
minimum and maximum values that can be calculated by summing
exactly four of the five integers. (The output can be greater
than a 32 bit integer.)

Sample Input
1 2 3 4 5
Sample Output
10 14
'''


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    length = len(arr)
    i = 0
    j = length - 1
    sort_arr = sorted(arr)
    for _ in sort_arr:
        minimum += sort_arr[i]
        i += 1
        maximum += sort_arr[j]
        j -= 1
        if i == length - 1:
            break
    print(minimum, maximum)


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
    arr = [3, 5, 9, 1, 7]
    miniMaxSum(arr)
