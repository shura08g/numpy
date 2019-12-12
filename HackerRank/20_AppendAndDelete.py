'''
You have a string of lowercase English alphabetic letters. You can perform two
types of operations on the string:
  1. Append a lowercase English alphabetic letter to the end of the string.
  2. Delete the last character in the string. Performing this operation on an
  empty string results in an empty string.
Given an integer, k, and two strings, s and t, determine whether or not you can
convert s to t by performing exactly k of the above operations on s. If it's
possible, print Yes. Otherwise, print No.

For example, strings s = [a, b, c] and t = [d, e, f]. Our number of moves,
k = 6. To convert s to t, we first delete all of the characters in 3 moves.
Next we add each of the characters of t in order. On the 6-th move, you will
have the matching string. If there had been more moves available, they could
have been eliminated by performing multiple deletions on an empty string. If
there were fewer than 6 moves, we would not have succeeded in creating the new
string.

Input Format
The first line contains a string s, the initial string.
The second line contains a string t, the desired final string.
The third line contains an integer k, the number of operations.

Output Format
Print Yes if you can obtain string t by performing exactly k operations on s.
Otherwise, print No.

Sample Input 0
hackerhappy
hackerrank
9

Sample Output 0
Yes

Explanation 0
We perform 5 delete operations to reduce string s to hacker. Next, we perform 4
append operations (i.e., r, a, n, and k), to get hackerrank. Because we were
able to convert s to t by performing exactly k = 9 operations, we print Yes.

Sample Input 1
aba
aba
7

Sample Output 1
Yes

Explanation 1
We perform 4 delete operations to reduce string s to the empty string (recall
that, though the string will be empty after 3 deletions, we can still perform
a delete operation on an empty string to get the empty string). Next, we
perform 3 append operations (i.e., a, b, and a). Because we were able to
convert s to t by performing exactly k = 7 operations, we print Yes.

Sample Input 2
ashley
ash
2

Sample Output 2
No

Explanation 2
To convert ashley to ash a minimum of 3 steps are needed. Hence we print No as
answer.
'''


# Complete the appendAndDelete function below.
def appendAndDelete22(s, t, k):
    s_length = len(s)
    t_length = len(t)
    if s_length + t_length < k:
        return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l:
            same += 1
        else:
            break

    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t
    if difference <= k and difference % 2 == k % 2:
        return 'Yes'
    return 'No'


def appendAndDelete(s, t, k):
    match = 0
    len_s = len(s)
    len_t = len(t)
    min_len = min(len_s, len_t)
    max_len = max(len_s, len_t)
    if len_s + len_t < k:
        return 'Yes'
    if max_len - min_len > k:
        return 'No'
    for i in range(min_len):
        if s[i] == t[i]:
            match += 1
        else:
            break
    if len_s - match > k:
        return 'No'
    diff = (len_s - match) + (len_t - match)
    if diff <= k and diff % 2 == k % 2:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # t = input()
    # k = int(input())
    # result = appendAndDelete(s, t, k)
    # fptr.write(result + '\n')
    # fptr.close()
    s = 'hackerhappy'
    t = 'hackerrank'
    k = 9
    result = appendAndDelete(s, t, k)
    print(result)  # 'Yes'

    s = 'aba'
    t = 'aba'
    k = 7
    result = appendAndDelete(s, t, k)
    print(result)  # 'Yes'

    s = 'ashley'
    t = 'ash'
    k = 2
    result = appendAndDelete(s, t, k)
    print(result)  # 'No'

    s = 'y'
    t = 'yu'
    k = 2
    result = appendAndDelete(s, t, k)
    print(result)  # 'No'

    s = 'zzzzz'
    t = 'zzzzzzz'
    k = 4
    result = appendAndDelete(s, t, k)
    print(result)  # 'Yes'

    s = 'abcd'
    t = 'abcdert'
    k = 10
    result = appendAndDelete(s, t, k)
    print(result)  # 'No'
