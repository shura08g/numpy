'''
Aerith is playing a cloud hopping game. In this game, there are sequentially
numbered clouds that can be thunderheads or cumulus clouds. Her character must
jump from cloud to cloud until it reaches the start again.

To play, Aerith is given an array of clouds, c and an energy level e = 100. She
starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud
c[(i+k)%n]. If Aerith lands on a thundercloud, c[i] = 1, her energy (e)
decreases by 2 additional units. The game ends when Aerith lands back on
cloud 0.

Given the values of n, k, and the configuration of the clouds as an array c,
can you determine the final value of e after the game ends?

For example, give c = [0, 0, 1, 0] and k = 2, the indices of her path are
0 -> 2 -> 0. Her energy level reduces by 1 for each jump to 98. She landed on
one thunderhead at an additional cost of 2 energy units. Her final energy level
is 96.

Note: Recall that % refers to the modulo operation. In this case, it serves to
make the route circular. If Aerith is at c[n-1] and jumps 1, she will arrive
at c[0].

Input Format
The first line contains two space-separated integers, n and k, the number of
clouds and the jump distance.
The second line contains n space-separated integers c[i] where 0 <= i <= n.
Each cloud is described as follows:
  If c[i] = 0, then cloud i is a cumulus cloud.
  If c[i] = 1, then cloud i is a thunderhead.

Output Format
Print the final value of e on a new line.

Sample Input
8 2
0 0 1 0 0 1 1 0

Sample Output
92

Explanation
Observe that our thunderheads are the clouds numbered 2, 5, and 6.
Aerith makes the following sequence of moves:
1. Move: 0 -> 2, Energy: e = 100 - 1 - 2 = 97.
2. Move: 2 -> 4, Energy: e = 97 - 1 = 96.
3. Move: 4 -> 6, Energy: e = 96 - 1 - 2 = 93.
4. Move: 6 -> 0, Energy: e = 93 - 1 = 92.
'''


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    result = 100
    length = len(c)
    i = k % length
    result -= c[i] * 2 + 1
    while i != 0:
        i = (i + k) % length
        result -= c[i] * 2 + 1
    return result


def jumpingOnClouds2(c, k):
    result = 100
    length = len(c)
    i = 0
    while i < length:
        print(result, i)
        if c[i] == 0:
            result -= 1
        else:
            result -= 3
        i = i + k
        if i >= length:
            i = i % length
        if i == 0:
            break
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # c = list(map(int, input().rstrip().split()))
    # result = jumpingOnClouds(c, k)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    k = 2
    c = [0, 0, 1, 0, 0, 1, 1, 0]
    result = jumpingOnClouds(c, k)
    print(result)  # 92

    k = 3
    c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    result = jumpingOnClouds(c, k)
    print(result)  # 80
