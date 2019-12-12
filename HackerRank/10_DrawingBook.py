'''
Brie’s Drawing teacher asks her class to open their books to a page number.
Brie can either start turning pages from the front of the book or from the back
of the book. She always turns pages one at a time. When she opens the book,
page 1 is always on the right side:

When she flips page 1, she sees pages 2 and 3. Each page except the last page
will always be printed on both sides. The last page may only be printed on the
front, given the length of the book. If the book is n pages long, and she wants
to turn to page p, what is the minimum number of pages she will turn? She can
start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages Brie must turn in
order to arrive at page p.

Output Format
Print an integer denoting the minimum number of pages Brie must turn to get
to page p.

Sample Input 0
6
2

Sample Output 0
1

Explanation 0
If Brie starts turning from page 1, she only needs to turn 1 page:
If Brie starts turning from page 6, she needs to turn 2 pages:

Sample Input 1
5
4

Sample Output 1
0

Explanation 1
If Brie starts turning from page 1, she needs to turn 2 pages:
If Brie starts turning from page 5, she doesn't need to turn any pages:
Because we want to print the minimum number of page turns, we print 0 as
our answer.
'''


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    return min(p // 2, (n // 2 - p // 2))


def pageCount2(n, p):
    if n // 2 >= p:  # from begin
        return p // 2
    else:  # from end
        return n // 2 - p // 2


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # p = int(input())

    n = 6
    p = 2
    result = pageCount(n, p)
    print(n, p, result)  # 1

    n = 5
    p = 4
    result = pageCount(n, p)
    print(n, p, result)  # 0

    n = 7
    p = 3
    result = pageCount(n, p)
    print(n, p, result)  # 1

    n = 6
    p = 5
    result = pageCount(n, p)
    print(n, p, result)  # 1

    n = 6
    p = 4
    result = pageCount(n, p)
    print(n, p, result)  # 1

    n = 4
    p = 4
    result = pageCount(n, p)
    print(n, p, result)  # 0

    n = 4
    p = 1
    result = pageCount(n, p)
    print(n, p, result)  # 0

    n = 5
    p = 5
    result = pageCount(n, p)
    print(n, p, result)  # 0

    n = 5
    p = 1
    result = pageCount(n, p)
    print(n, p, result)  # 0

    # fptr.write(str(result) + '\n')
    # fptr.close()
