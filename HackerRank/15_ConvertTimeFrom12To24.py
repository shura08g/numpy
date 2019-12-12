'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour
clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format
A single string s containing a time in 12-hour clock format (i.e.:hh:mm:ssAM
or hh:mm:ssPM), where 01<=hh<=12 and 00<=mm, ss<=59.

Constraints
All input times are valid

Output Format
Convert and print the given time in 24-hour format, where 00<=hh<=23.

Sample Input 0
07:05:45PM
Sample Output 0
19:05:45
'''


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s[-2:]
    hms = s[:-2].split(':')
    if time == 'AM':
        if hms[0] == '12':
            hms[0] = '00'
            return ':'.join(hms)
        return s[:-2]
    elif time == 'PM':
        if hms[0] == '12':
            return ':'.join(hms)
        hour = int(hms[0])
        hour += 12
        hms[0] = str(hour)
        return ':'.join(hms)
    else:
        return 'Unknown format'


if __name__ == '__main__':
    # f = open('8_test.txt', 'w')
    # s = input()
    s = '07:05:45AM'
    result = timeConversion(s)
    print(result)
    s = '07:05:45PM'
    result = timeConversion(s)
    print(result)
    s = '12:00:00AM'
    result = timeConversion(s)
    print(result)
    s = '12:00:00PM'
    result = timeConversion(s)
    print(result)
    s = '12:05:00AM'
    result = timeConversion(s)
    print(result)
    s = '12:05:00PM'
    result = timeConversion(s)
    print(result)
    # f.write(result + '\n')
    # f.close()
