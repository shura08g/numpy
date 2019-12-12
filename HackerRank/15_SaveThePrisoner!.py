'''
A jail has a number of prisoners and a number of treats to pass out to them.
Their jailer decides the fairest way to divide the treats is to seat the
prisoners around a circular table in sequentially numbered chairs. A chair
number will be drawn from a hat. Beginning with the prisoner in that chair,
one candy will be handed to each prisoner sequentially around the table until
all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like
all the others, but it tastes awful. Determine the chair number occupied by the
prisoner who will receive that candy.

For example, there are 4 prisoners and 6 pieces of candy. The prisoners arrange
themselves in seats numbered 1 to 4. Let's suppose two is drawn from the hat.
Prisoners receive candy at positions 2, 3, 4, 1, 2, 3. The prisoner to be
warned sits in chair number 3.

Input Format
The first line contains an integer, t, denoting the number of test cases.
The next t lines each contain 3 space-separated integers:
- n: the number of prisoners
- m: the number of sweets
- s: the chair number to start passing out treats at

Output Format
For each test case, print the chair number of the prisoner who receives the
awful treat on a new line.

Sample Input 0
2
5 2 1
5 2 2

Sample Output 0
2
3

Explanation 0
In first query, there are n = 5 prisoners and m = 2 sweets. Distribution
starts at seat number s = 1. Prisoners in seats numbered 1 and 2 get sweets.
Warn prisoner 2.
In the second query, distribution starts at seat 2 so prisoners in seats 2 and
3 get sweets. Warn prisoner 3.

Sample Input 1
2
7 19 2
3 7 3

Sample Output 1
6
3

Explanation 1
In the first test case, there are n = 7 prisoners, m = 19 sweets and they are
passed out starting at chair s = 2. The candies go all around twice and there
are 5 more candies passed to each prisoner from seat 2 to seat 6.
In the second test case, there are n = 3 prisoners, m = 7 candies and they are
passed out starting at seat s = 3. They go around twice, and there is one more
to pass out to the prisoner at seat 3.
'''


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    result = 0
    result = (m + s - 1) % n
    if result == 0:
        return n
    else:
        return result


def saveThePrisoner2(n, m, s):
    result = 0
    end = 0
    if m > n:
        if m % n == 0:
            end = n
        else:
            end = m % n
    else:
        end = m
    if (s + end) <= n + 1:
        result = s + end - 1
    else:
        result = s + end - n - 1
    # print(n, m, s, end)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input())
    # for t_itr in range(t):
    #     nms = input().split()
    #     n = int(nms[0])
    #     m = int(nms[1])
    #     s = int(nms[2])
    #     result = saveThePrisoner(n, m, s)
    #     fptr.write(str(result) + '\n')
    # fptr.close()

    n = 5
    m = 1
    s = 1
    result = saveThePrisoner(n, m, s)
    print(result)  # 1

    n = 5
    m = 2
    s = 1
    result = saveThePrisoner(n, m, s)
    print(result)  # 2

    n = 5
    m = 2
    s = 2
    result = saveThePrisoner(n, m, s)
    print(result)  # 3

    n = 7
    m = 19
    s = 2
    result = saveThePrisoner(n, m, s)
    print(result)  # 6

    n = 3
    m = 7
    s = 3
    result = saveThePrisoner(n, m, s)
    print(result)  # 3

    n = 352926151
    m = 380324688
    s = 94730870
    result = saveThePrisoner(n, m, s)
    print(result)  # 122129406

    n = 208526924
    m = 756265725
    s = 150817879
    result = saveThePrisoner(n, m, s)
    print(result)  # 72975907

    n = 499999999
    m = 999999997
    s = 2
    result = saveThePrisoner(n, m, s)
    print(result)  # 499999999

    n = 499999999
    m = 999999998
    s = 2
    result = saveThePrisoner(n, m, s)
    print(result)  # 1

    n = 999999999
    m = 999999999
    s = 1
    result = saveThePrisoner(n, m, s)
    print(result)  # 999999999

    n = 13
    m = 140874526
    s = 1
    result = saveThePrisoner(n, m, s)
    print(result)  # 13
