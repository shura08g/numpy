'''
You are given an array of n integers, ar = [], and a positive integer, k.
Find and print the number of (i, j) pairs where i < j and ar[i] + ar[j] is
divisible by k.

Input Format
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar

Output Format
Print the number of (i, j) pairs where i < j and ar[i] + ar[j] is evenly
divisible by k.

Sample Input
6 3
1 3 2 6 1 2

Sample Output
5
'''


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                print(i, j)
                result += 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # ar = list(map(int, input().rstrip().split()))

    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    result = divisibleSumPairs(n, k, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
