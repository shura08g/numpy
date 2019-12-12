'''
We define a magic square to be an n x n matrix of distinct positive integers
from 1 to n^2 where the sum of any row, column, or diagonal of length n is
always equal to the same number: the magic constant.

You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9].
We can convert any digit a to any other digit b in the range [1, 9] at cost
of |a - b|. Given s, convert it into a magic square at minimal cost. Print
this cost on a new line.

Note: The resulting magic square must contain distinct integers in the
inclusive range [1, 9].

For example, we start with the following matrix s:
5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2

This took three replacements at a cost of |5 - 8| + |8 - 9| + |4 - 7| = 7.

Input Format
Each of the lines contains three space-separated integers of row s[i].

Output Format
Print an integer denoting the minimum cost of turning matrix s into a magic
square.

Sample Input 0
4 9 2
3 5 7
8 1 5

Sample Output 0
1

Explanation 0
If we change the bottom right value, s[2][2], from 5 to 6 at a cost of
|6 - 5| = 1, s becomes a magic square at the minimum possible cost.

Sample Input 1
4 8 2
4 5 7
6 1 6

Sample Output 1
4

Explanation 1
Using 0-based indexing, if we make
s[0][1]->9 at a cost of |9 - 8| = 1
s[1][0]->3 at a cost of |3 - 4| = 1
s[2][0]->8 at a cost of |8 - 6| = 2,
then the total cost will be 1 + 1 + 2 = 4.
'''


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    all_possible = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    diffs = []
    for possiblity in all_possible:
        # zip_lst = list(zip(possiblity, s))
        # print(zip_lst)
        cost = 0
        for p_row, s_row in list(zip(possiblity, s)):
            # p_zip = list(zip(p_row, s_row))
            for p_num, s_num in (list(zip(p_row, s_row))):
                if p_num != s_num:
                    cost += abs(p_num - s_num)
                    # print(p_zip)
        diffs.append(cost)
    return min(diffs)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = []
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().split())))

    s = [[5, 3, 4],
         [1, 5, 8],
         [6, 4, 2]]
    result = formingMagicSquare(s)
    print(result)  # 7

    s = [[4, 9, 2],
         [3, 5, 7],
         [8, 1, 5]]
    result = formingMagicSquare(s)
    print(result)  # 1

    s = [[4, 8, 2],
         [4, 5, 7],
         [6, 1, 6]]
    result = formingMagicSquare(s)
    print(result)  # 4

    # fptr.write(str(result) + '\n')
    # fptr.close()
