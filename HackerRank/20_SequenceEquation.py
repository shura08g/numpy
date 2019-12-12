'''
Given a sequence of n integers, where each element is distinct and satisfies
1 <= p(x) <= n. For each x where 1 <= x <= n, find any integer y such that
p(p(y)) = x and print the value of y on a new line.

For example, assume the sequence p = [5, 2, 1, 3, 4]. Each value of x between
1 and 5, the length of the sequence, is analyzed as follows:

1. x = 1 = p[3], p[4] = 3, so p[p[4]] = 1
2. x = 2 = p[2], p[2] = 2, so p[p[2]] = 2
3. x = 3 = p[4], p[5] = 4, so p[p[5]] = 3
4. x = 4 = p[5], p[1] = 5, so p[p[1]] = 4
5. x = 5 = p[1], p[3] = 1, so p[p[3]] = 5
The values for y are [4, 2, 5, 1, 3].

Sample Input 0
3
2 3 1

Sample Output 0
2
3
1

Explanation 0
Given the values of p(1) = 2, p(2) = 3, and p(3) = 1, we calculate and print
the following values for each x from 1 to n:

1. x = 1 = p(3) = p(p(2)) = p(p(y)), so we print the value of 2 on a new line.
2. x = 2 = p(1) = p(p(3)) = p(p(y)), so we print the value of 3 on a new line.
1. x = 3 = p(2) = p(p(1)) = p(p(y)), so we print the value of 1 on a new line.

Sample Input 1
5
4 3 5 1 2

Sample Output 1
1
3
5
4
2
'''


# Complete the permutationEquation function below.
def permutationEquation(p):
    length = len(p)
    result = []
    for i in range(1, length + 1):
        index = p.index(i) + 1
        next_index = p.index(index) + 1
        result.append(next_index)
    return result


def permutationEquation2(p):
    length = len(p)
    result = []
    for i in range(1, length + 1):
        index = 0
        next_index = 0
        for j in range(length):
            if i == p[j]:
                index = j + 1
                for x in range(length):
                    if index == p[x]:
                        next_index = x + 1
        result.append(next_index)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # p = list(map(int, input().rstrip().split()))
    # result = permutationEquation(p)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
    p = [5, 2, 1, 3, 4]
    result = permutationEquation(p)
    print(result)  # [4, 2, 5, 1, 3]

    p = [2, 3, 1]
    result = permutationEquation(p)
    print(result)  # [2, 3, 1]

    p = [4, 3, 5, 1, 2]
    result = permutationEquation(p)
    print(result)  # [1, 3, 5, 4, 2]
