'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
to small details like topography. During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U, or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down represents a 1
unit change in altitude. We define the following terms:
  A mountain is a sequence of consecutive steps above sea level, starting with
    a step up from sea level and ending with a step down to sea level.
  A valley is a sequence of consecutive steps below sea level, starting with a
    step down from sea level and ending with a step up to sea level.
  Given Gary's sequence of up and down steps during his last hike, find and
    print the number of valleys he walked through.

For example, if Gary's path is s = [DDUUUUDD], he first enters a valley 2 units
deep. Then he climbs out an up onto a mountain 2 units high. Finally, he
returns to sea level and ends his hike.

Input Format
The first line contains an integer n, the number of steps in Gary's hike.
The second line contains a single string s, of n characters that describe his
path.

Output Format
Print a single integer that denotes the number of valleys Gary walked through
during his hike.

Sample Input
8
UDDDUDUU

Sample Output
1
'''


# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count = 0
    current_state = 0
    up = 'U'
    for i in range(n):
        if s[i] == up:
            current_state += 1
            if current_state == 0:
                valley_count += 1
        else:
            current_state -= 1
    return valley_count


def countingValleys2(n, s):
    valley_count = 0
    current_state = 0
    i = 0
    while i < n:
        if s[i] == 'U':
            current_state += 1
            if current_state == 0:
                valley_count += 1
        else:
            current_state -= 1
        i = i + 1
    return valley_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # s = input()

    n = 8
    s = 'DDUUUUDD'
    result = countingValleys(n, s)
    print(result)  # 1

    n = 8
    s = 'UDDDUDUU'
    result = countingValleys(n, s)
    print(result)  # 1

    n = 8
    s = 'UUUUDDDD'
    result = countingValleys(n, s)
    print(result)  # 0

    n = 8
    s = 'DDDDUUUU'
    result = countingValleys(n, s)
    print(result)  # 1

    n = 12
    s = 'DDUUDDUDUUUD'
    result = countingValleys(n, s)
    print(result)  # 2

    # fptr.write(str(result) + '\n')
    # fptr.close()
