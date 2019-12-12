'''
John works at a clothing store. He has a large pile of socks that he must pair
by color for sale. Given an array of integers representing the color of each
sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2].
There is one pair of color 1 and one of color 2. There are three odd socks
left, one of each color. The number of pairs is 2.

Output Format
Return the total number of matching pairs of socks that John can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
'''


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set()
    pair_count = 0
    for i in ar:
        if i not in colors:
            colors.add(i)
        else:
            pair_count += 1
            colors.remove(i)
    return pair_count


def sockMerchant2(n, ar):
    pair_count = 0
    sorted_ar = sorted(ar)
    is_pair = True
    for i in range(1, len(sorted_ar)):
        if sorted_ar[i - 1] == sorted_ar[i] and is_pair:
            pair_count += 1
            is_pair = False
        else:
            is_pair = True
    return pair_count


def sockMerchant3(n, ar):
    pair_count = 0
    max_el = max(ar)
    template = [0] * max_el
    for val in ar:
        template[val - 1] += 1
    # print(template)
    for val in template:
        if val != 0:
            pair_count += val // 2
    return pair_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print(result)  # 3

    n = 10
    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    result = sockMerchant(n, ar)
    print(result)  # 4

    # fptr.write(str(result) + '\n')
    # fptr.close()
