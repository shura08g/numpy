'''
Lily likes to play games with integers. She has created a new game where she
determines the difference between a number and its reverse. For instance,
given the number 12, its reverse is 21. Their difference is 9. The number
120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered
range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i...j] and a number k, determine the number
of days in the range that are beautiful. Beautiful numbers are defined as
numbers where |i - reverse(i)| is evenly divisible by k. If a day's value is
a beautiful number, it is a beautiful day. Print the number of beautiful days
in the range.

Function Description
Complete the beautifulDays function in the editor below. It must return the
number of beautiful days in the range.

beautifulDays has the following parameter(s):
i: the starting day number
j: the ending day number
k: the divisor

Input Format
A single line of three space-separated integers describing the respective
values of i, j, and k.

Output Format
Print the number of beautiful days in the inclusive range between i and j.

Sample Input
20 23 6

Sample Output
2

Explanation
Lily may go to the movies on days 20, 21, 22, and 23. We perform the following
calculations to determine which days are beautiful:
- Day 20 is beautiful because the following evaluates to a whole number:
  |20 - 02| / 6 = 18 / 6 = 3
- Day 21 is not beautiful because the following doesn't evaluate to a whole
  number: |21 - 12| / 6 = 9 / 6 = 1.5
- Day 22 is beautiful because the following evaluates to a whole number:
  |22 - 22| / 6 = 0 / 6 = 0
- Day 23 is not beautiful because the following doesn't evaluate to a whole
  number: |23 - 32| / 6 = 9 / 6 = 1.5
Only two days, 20 and 22, in this interval are beautiful. Thus, we print 2
as our answer.
'''


# Complete the beautifulDays function below.
def beautifulDays__(i, j, k):
    beautiful = [1 for day in range(i, j + 1)
                 if (day - int(str(day)[::-1])) % k == 0]
    # print(beautiful)
    return sum(beautiful)


def beautifulDays(i, j, k):
    result = 0
    for val in range(i, j + 1):
        if (abs(val - int(str(val)[::-1])) % k) == 0:
            result += 1
    return result


def reverse_num(num):
    temp = str(num)
    return int(temp[::-1])


def beautifulDays3(i, j, k):
    result = 0
    for val in range(i, j + 1):
        if (abs(val - reverse_num(val)) / k).is_integer():
            result += 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # ijk = input().split()
    # i = int(ijk[0])
    # j = int(ijk[1])
    # k = int(ijk[2])
    # result = beautifulDays(i, j, k)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    i = 20
    j = 23
    k = 6
    result = beautifulDays(i, j, k)
    print(result)  # 2

    i = 13
    j = 45
    k = 3
    result = beautifulDays(i, j, k)
    print(result)  # 33
