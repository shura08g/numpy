'''
You will be given two arrays of integers and asked to determine all integers
that satisfy the following two conditions:
 1.The elements of the first array are all factors of the integer being
 considered
 2.The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must
determine how many such numbers exist.

Input Format
The first line contains two space-separated integers, n and m, the number of
elements in array a and the number of elements in array b.
The second line contains n distinct space-separated integers describing a[i]
The third line contains m distinct space-separated integers describing b[j]

Output Format
Print the number of integers that are considered to be between a and b.

Sample Input
2 3
2 4
16 32 96
Sample Output
3
'''


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def lcm(a, b):
    greater = max(a, b)
    while True:
        if (greater % a) == 0 and (greater % b) == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def getTotalX(a, b):
    result = []
    count = 0
    # lcm_a = a[0]
    # for i in a[1:]:
    #     lcm_a = lcm(lcm_a, i)

    # gcd_b = b[0]
    # for i in b[1:]:
    #     gcd_b = gcd(gcd_b, i)

    for i in range(a[len(a) - 1], b[0] + 1):
        if (b[0] % i) == 0:
            result.append(i)
    for i in result:
        check_b = True
        for bi in b:
            if bi % i != 0:
                check_b = False
                break
        check_a = True
        for ai in a:
            if i % ai != 0:
                check_a = False
        if check_a and check_b:
            count += 1
    print(result)
    return count


def getTotalX2(a, b):
    last_a = a[len(a) - 1]
    first_b = b[0]
    count = 0
    for i in range(last_a, first_b + 1):
        check_b = True
        for bi in b:
            if bi % i != 0:
                check_b = False
                break
        check_a = True
        for ai in a:
            if i % ai != 0:
                check_a = False
                break
        if check_a and check_b:
            count += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # m = int(first_multiple_input[1])
    # arr = list(map(int, input().rstrip().split()))
    # brr = list(map(int, input().rstrip().split()))

    arr = [2, 6]
    brr = [24, 36]
    total = getTotalX(arr, brr)
    print(total)  # 2

    arr = [2, 4]
    brr = [16, 32, 96]
    total = getTotalX(arr, brr)
    print(total)  # 3

    arr = [2, 3, 6]
    brr = [42, 84]
    total = getTotalX(arr, brr)
    print(total)  # 2
    # fptr.write(str(total) + '\n')
    # fptr.close()
