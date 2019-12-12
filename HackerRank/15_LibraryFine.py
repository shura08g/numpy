'''
Your local library needs your help! Given the expected and actual return dates
for a library book, create a program that calculates the fine (if any). The fee
structure is as follows:
1. If the book is returned on or before the expected return date, no fine will
   be charged (i.e.: fine = 0).
2. If the book is returned after the expected return day but still within the
   same calendar month and year as the expected return date,
   fine = 15 Hackos * (the number of days late).
3. If the book is returned after the expected return month but still within
   the same calendar year as the expected return date, the.
   fine = 500 Hackos * (the number of months late).
4. If the book is returned after the calendar year in which it was expected,
   there is a fixed fine of 10000 Hackos.
Charges are based only on the least precise measure of lateness. For example,
whether a book is due January 1, 2017 or December 31, 2017, if it is returned
January 1, 2018, that is a year late and the fine would be 10000 Hackos.

Output Format
Print a single integer denoting the library fine for the book received
as input.

Sample Input
9 6 2015
6 6 2015

Sample Output
45

Explanation
Given the following dates:
Returned: d1 = 9, m1 = 6, y1 = 2015
Due: d2 = 6, m2 = 6, y2 = 2015

Because y2 == y1, we know it is less than a year late.
Because m2 == m1, we know it's less than a month late.
Because d2 < d1, we know that it was returned late (but still within the same
month and year).

Per the library's fee structure, we know that our fine will be
15 Hacks * (# deys late). We then print the result of
15 * (d1 - d2) = 15 * (9 - 6) = 45 as our output.
'''


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1 > y2:
        fine = 10000
    elif y1 <= y2:
        if m1 > m2 and (y1 >= y2):
            fine = 500 * (m1 - m2)
        elif m1 <= m2:
            if (d1 > d2 and (m1 - m2 >= 0) and (y1 >= y2)):
                fine = 15 * (d1 - d2)
            else:
                fine = 0
    return fine


def libraryFine2(d1, m1, y1, d2, m2, y2):
    result = 0
    if y1 <= y2:
        if m1 < m2:
            return result
        if m1 == m2:
            if d1 <= d2:
                return result
            else:
                result = 15 * (d1 - d2)
                return result
        else:
            result = 500 * (m1 - m2)
            return result
    if y1 > y2:
        if m1 > m2:
            result = 10000
            return result
        if m1 == m2:
            if d1 >= d2:
                result = 10000
                return result
            else:
                result = 500 * (m1 - m2)
                return result
        if m1 < m2:
            result = 500 * (12 + m1 - m2)
            return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # d1M1Y1 = input().split()
    # d1 = int(d1M1Y1[0])
    # m1 = int(d1M1Y1[1])
    # y1 = int(d1M1Y1[2])
    # d2M2Y2 = input().split()
    # d2 = int(d2M2Y2[0])
    # m2 = int(d2M2Y2[1])
    # y2 = int(d2M2Y2[2])
    # result = libraryFine(d1, m1, y1, d2, m2, y2)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    d1 = 9
    m1 = 6
    y1 = 2015
    d2 = 6
    m2 = 6
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 45

    d1 = 9
    m1 = 6
    y1 = 2015
    d2 = 6
    m2 = 4
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 1000

    d1 = 9
    m1 = 6
    y1 = 2015
    d2 = 6
    m2 = 8
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 0

    d1 = 9
    m1 = 6
    y1 = 2016
    d2 = 6
    m2 = 8
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 10000

    d1 = 1
    m1 = 1
    y1 = 2016
    d2 = 1
    m2 = 1
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 10000

    d1 = 1
    m1 = 1
    y1 = 2016
    d2 = 1
    m2 = 1
    y2 = 2015
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)  # 10000
