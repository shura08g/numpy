'''
Lily has a chocolate bar that she wants to share it with Ron for his birthday.
Each of the squares has an integer on it. She decides to share a contiguous
segment of the bar selected such that the length of the segment matches Ron's
birth month and the sum of the integers on the squares is equal to his birth
day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, s= [2, 2, 1, 3, 2]. She
wants to find segments summing to Ron's birth day, d = 4 with a length
equalling his birth month, m = 2. In this case, there are two segments meeting
her criteria: [2, 3] and [1, 3].

Input Format
The first line contains an integer n, the number of squares in the chocolate
bar.
The second line contains n space-separated integers s[i], the numbers on the
chocolate squares where 0 <= i < n.
The third line contains two space-separated integers, d and m, Ron's birth day
and his birth month.

Output Format
Print an integer denoting the total number of ways that Lily can portion her
chocolate bar to share with Ron.

Sample Input 0
5
1 2 1 3 2
3 2
Sample Output 0
2

Sample Input 1
6
1 1 1 1 1 1
3 2
Sample Output 1
0

Sample Input 2
1
4
4 1
Sample Output 2
1
'''


# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    for i in range(0, len(s)):
        if sum(s[i:m + i]) == d and i <= (len(s) - m):
            result += 1
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    # s = list(map(int, input().rstrip().split()))
    # dm = input().rstrip().split()
    # d = int(dm[0])
    # m = int(dm[1])

    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    result = birthday(s, d, m)
    print(result)

    s = [1, 1, 1, 1, 1, 1]
    d = 3
    m = 2
    result = birthday(s, d, m)
    print(result)

    s = [4]
    d = 4
    m = 1
    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
