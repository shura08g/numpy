'''
Given an array of integers, find and print the maximum number of integers you
can select from the array such that the absolute difference between any two of
the chosen integers is less than or equal to 1. For example, if your array is
a = [1, 1, 2, 2, 4, 4, 5, 5, 5], you can create two subarrays meeting the
criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has
5 elements.

Input Format
The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers a[i].

Output Format
A single integer denoting the maximum number of integers you can choose from
the array such that the absolute difference between any two of the chosen
integers is <= 1.

Sample Input 0
6
4 6 5 3 3 1

Sample Output 0
3

Explanation 0
We choose the following multiset of integers from the array: {4, 3, 3}. Each
pair in the multiset has an absolute difference <= 1 (i.e., |4 - 3| = 1 and
|3 - 3| = 0), so we print the number of chosen integers, 3, as our answer.

Sample Input 1
6
1 2 2 3 1 2

Sample Output 1
5

Explanation 1
We choose the following multiset of integers from the array: {1, 2, 2, 1, 2}.
Each pair in the multiset has an absolute difference <= 1 (i.e., |1 - 2| = 1,
|1 - 1| = 0, and |2 - 2| = 0), so we print the number of chosen integers, 5,
as our answer.
'''


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    result = 0
    temp = [0] * (max(a) + 1)
    for val in a:
        temp[val] += 1
    for i in range(1, len(temp) - 1):
        result = max(result, temp[i] + temp[i + 1])
    return result


def pickingNumbers2(a):
    result = 0
    length = len(a)
    for i in range(length):
        for j in range(length):
            count = 0
            if abs(a[i] - a[j]) <= 1:
                for val in a:
                    if val == a[i] or val == a[j]:
                        count += 1
                if result < count:
                    result = count
    return result


def pickingNumbers3(a):
    result = 0
    temp = []
    length = len(a)
    for i in range(length):
        for j in range(length):
            if abs(a[i] - a[j]) <= 1:
                for val in a:
                    if val == a[i] or val == a[j]:
                        temp.append(val)
                if result < len(temp):
                    result = len(temp)
            else:
                continue
            temp.clear()
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # a = list(map(int, input().rstrip().split()))

    a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
    result = pickingNumbers(a)
    print(result)  # 5

    a = [4, 6, 5, 3, 3, 1]
    result = pickingNumbers(a)
    print(result)  # 3

    a = [1, 2, 2, 3, 1, 2]
    result = pickingNumbers(a)
    print(result)  # 5

    # fptr.write(str(result) + '\n')
    # fptr.close()
