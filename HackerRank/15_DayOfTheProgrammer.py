'''
Marie invented a Time Machine and wants to test it by time-traveling to visit
Russia on the Day of the Programmer (the 256-th day of the year) during a year
in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since
1919 they used the Gregorian calendar system. The transition from the Julian to
Gregorian calendar system occurred in 1918, when the next day after January
31-st was February 14-th. This means that in 1918, February 14-th was the 32-nd
day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of
days; it has 29 days during a leap year, and 28 days during all other years.
In the Julian calendar, leap years are divisible by 4; in the Gregorian
calendar, leap years are either of the following:
  Divisible by 400.
  Divisible by 4 and not divisible by 100.

Given a year, y, find the date of the 256-th day of that year according to the
official Russian calendar during that year. Then print it in the format
dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and
yyyy is y.

For example, the given year = 1984. 1984 is divisible by 4, so it is a leap
year. The 256-th day of a leap year after 1918 is September 12, so the answer
is 12.09.1984.

Input Format
A single integer denoting year y.

Constraints
  1700 <= y <= 2700

Output Format
Print the full date of Day of the Programmer during year y in the format
dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy
is y.

Sample Input 0
2017

Sample Output 0
13.09.2017

Sample Input 1
2016

Sample Output 1
12.09.2016


Sample Input 2
1800

Sample Output 2
12.09.1800
'''


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    # sum_8_month = 243  # 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    # sum_8_month_leap = 244  # 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
    # programmer_day = 256
    pd = '13.09.'
    pd_leap = '12.09.'
    pd_1918 = '26.09.1918'
    result = ''
    # if (year % 4) == 0:
    #     if (year % 100) == 0:
    #         if (year % 400) == 0:
    #             result = pd_leap + str(year)
    #         else:
    #             result = pd + str(year)
    #     else:
    #         result = pd_leap + str(year)
    # else:
    #     result = pd + str(year)
    if year == 1918:
        return pd_1918
    elif year > 1918:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            result = pd + str(year)
        else:
            result = pd_leap + str(year)
    else:
        if year % 4 == 0:
            result = pd_leap + str(year)
        else:
            result = pd + str(year)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # year = int(input().strip())

    year = 2017
    result = dayOfProgrammer(year)
    print(result)  # 13.09.2017

    year = 2016
    result = dayOfProgrammer(year)
    print(result)  # 12.09.2017

    year = 1800
    result = dayOfProgrammer(year)
    print(result)  # 12.09.2017

    year = 2100
    result = dayOfProgrammer(year)
    print(result)  # 13.09.2017

    year = 2000
    result = dayOfProgrammer(year)
    print(result)  # 12.09.2017

    year = 1918
    result = dayOfProgrammer(year)
    print(result)  # 26.09.2017

    # fptr.write(result + '\n')
    # fptr.close()
