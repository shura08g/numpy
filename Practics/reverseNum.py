# n = int(input("Input number"))
n = 77577577
lstNum = [459, 556, 74899, 78987, 7567, 77577]


def reverseNumber(number):
    revNum = 0
    while number != 0:
        rem = number % 10
        revNum = revNum * 10 + rem
        # print(number, rem, revNum)
        number //= 10
    return revNum


def isPalindrome(number):
    if number == reverseNumber(number):
        return True
    return False


print(reverseNumber(n))


if isPalindrome(n):
    print("{} is palindrome".format(n))

for val in lstNum:
    print(reverseNumber(val))
    if isPalindrome(val):
        print("{} is palindrome".format(val))
