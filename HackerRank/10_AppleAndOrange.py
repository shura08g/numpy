'''
Sam's house has an apple tree and an orange tree that yield an abundance
of fruit. The apple tree is to the left of his house, and the orange tree
is to its right. You can assume the trees are located on a single point,
where the apple tree is at point a, and the orange tree is at point b.

When a fruit falls from its tree, it lands d units of distance from its tree
of origin along the x-axis. A negative value of d means the fruit fell d units
to the tree's left, and a positive value of d means it falls d units to the
tree's right.
Given the value of d for m apples and n oranges, determine how many apples and
oranges will fall on Sam's house (i.e., in the inclusive range [s, t])?

For example, Sam's house is between s = 7 and yt = 10. The apple tree is
located at a = 4 and the orange at b = 12. There are m = 3 apples and n = 3
oranges. Apples are thrown apples = [2, 3, -4] units distance from a, and
oranges = [3, -2, -4] units distance. Adding each apple distance to the
position of the tree, they land at [4 + 2, 4 + 3, 4 + -4] = [6, 7, 0].
Oranges land at [12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]. One apple and
two oranges land in the inclusive range 7 - 10 so we print
1
2

Input Format
 The first line contains two space-separated integers denoting the respective
 values of s and t.
 The second line contains two space-separated integers denoting the respective
 values of a and b.
 The third line contains two space-separated integers denoting the respective
 values of m and n.
 The fourth line contains m space-separated integers denoting the respective
 distances that each apple falls from point a.
 The fifth line contains n space-separated integers denoting the respective
 distances that each orange falls from point b.

Sample Input 0
7 11
5 15
3 2
-2 2 1
5 -6
Sample Output 0
1
1
'''


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for apple in apples:
        if (apple + a) in range(s, t + 1):
            apples_count += 1
    for orange in oranges:
        if (orange + b) in range(s, t + 1):
            oranges_count += 1
    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    # st = input().split()
    # s = int(st[0])
    # t = int(st[1])
    # ab = input().split()
    # a = int(ab[0])
    # b = int(ab[1])
    # mn = input().split()
    # m = int(mn[0])
    # n = int(mn[1])
    # apples = list(map(int, input().rstrip().split()))
    # oranges = list(map(int, input().rstrip().split()))
    s = 7
    t = 11
    a = 5
    b = 15
    m = 3
    n = 2
    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)

    s = 7
    t = 10
    a = 4
    b = 12
    m = 3
    n = 3
    apples = [2, 3, -4]
    oranges = [3, -2, -4]

    countApplesAndOranges(s, t, a, b, apples, oranges)
