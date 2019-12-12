def simpleArraySum(ar):
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':
    ar = [1, 2, 3, 4, 10, 11]
    result = simpleArraySum(ar)
    print(result)
