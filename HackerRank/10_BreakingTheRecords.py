'''
Maria plays college basketball and wants to go pro. Each season she maintains
a record of her play. She tabulates the number of times she breaks her season
record for most points and least points in a game. Points scored in the first
game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array
score = [12, 24, 10, 24]. Scores are in the same order as the games played.
She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1

Input Format
The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective
values of score

Output Format
Print two space-seperated integers describing the respective numbers of times
her best (highest) score increased and her worst (lowest) score decreased.

Sample Input 0
9
10 5 20 20 4 5 2 25 1

Sample Output 0
2 4


Sample Input 1
10
3 4 21 36 10 28 35 5 24 42

Sample Output 1
4 0
'''


# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_num = scores[0]
    max_num = scores[0]
    min_count = 0
    max_count = 0
    for val in scores[1:]:
        if val > max_num:
            max_count += 1
            max_num = val
        if val < min_num:
            min_count += 1
            min_num = val
    return (max_count, min_count)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # scores = list(map(int, input().rstrip().split()))

    scores = [12, 24, 10, 24]
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))

    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))

    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
