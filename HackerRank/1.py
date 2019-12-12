# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            result[0] += 1
        if a[i] < b[i]:
            result[1] += 1
    return result

if __name__ == '__main__':
    fptr = open('1_test.txt', 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
