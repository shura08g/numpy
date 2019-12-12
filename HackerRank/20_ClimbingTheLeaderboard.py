'''
Alice is playing an arcade game and wants to climb to the top of the
leaderboard and wants to track her ranking. The game uses Dense Ranking,
so its leaderboard works like this:
  The player with the highest score is ranked number 1 on the leaderboard.
  Players who have equal scores receive the same ranking number, and the next
   player(s) receive the immediately following ranking number.

For example, the four players on the leaderboard have high scores of
100, 90, 90 and 80. Those players will have ranks 1, 2, 2, and 3, respectively.
If Alice's scores are 70, 80 and 105, her rankings after each game are 4-th,
3-rd and 1-st.

Input Format
The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers scores[i], the leaderboard
scores in decreasing order.
The next line contains an integer, m, denoting the number games Alice plays.
The last line contains m space-separated integers alice[j], the game scores.

Constraints
The existing leaderboard, scores, is in descending order.
Alice's scores, alice, are in ascending order.

Output Format
Print m integers. The j-th integer should indicate Alice's rank after playing
the j-th game.

Sample Input 1
7
100 100 50 40 40 20 10
4
5 25 50 120

Sample Output 1
6
4
2
1

Sample Input 2
6
100 90 90 80 75 60
5
50 65 77 90 102

Sample Output 2
6
5
4
2
1
'''


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alices):
    unique_scores = list(reversed(sorted(set(scores))))
    i = len(alice) - 1
    j = 0
    result = []
    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
            result.append(j + 1)
            i -= 1
        else:
            j += 1
    return sorted(result, reverse=True)


def climbingLeaderboard2(scores, alice):
    result = []
    unique_score = list(set(scores))
    max_score = max(unique_score)
    for a_score in alice:
        rank = 1
        if a_score >= max_score:
            result.append(rank)
            break
        for score in unique_score:
            if a_score < score:
                rank += 1
        result.append(rank)
    return result


def climbingLeaderboard3(scores, alice):
    result = []
    max_score = max(scores)
    prev_score = 0
    for a_score in alice:
        rank = 1
        if a_score >= max_score:
            result.append(rank)
            break
        for score in scores:
            if a_score < score and prev_score != score:
                rank += 1
            prev_score = score
        result.append(rank)
    return result


def climbingLeaderboard4(scores, alice):
    result = []
    max_score = max(scores)
    prev_score = 0
    for a_score in alice:
        rank = 1
        i = 0
        if a_score >= max_score:
            result.append(rank)
            break
        for i in range(len(scores)):
            if a_score < scores[i] and prev_score != scores[i]:
                rank += 1
            prev_score = scores[i]
        result.append(rank)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # scores_count = int(input())
    # scores = list(map(int, input().rstrip().split()))
    # alice_count = int(input())
    # alice = list(map(int, input().rstrip().split()))

    scores = [100, 90, 90, 80]
    alice = [70, 80, 105]
    result = climbingLeaderboard(scores, alice)
    print(result)  # [4, 3, 1]

    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]
    result = climbingLeaderboard(scores, alice)
    print(result)  # [6, 4, 2, 1]

    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]
    result = climbingLeaderboard(scores, alice)
    print(result)  # [6, 5, 4, 2, 1]

    scores = [100, 100, 100]
    alice = [100]
    result = climbingLeaderboard(scores, alice)
    print(result)  # [6, 5, 4, 2, 1]

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
