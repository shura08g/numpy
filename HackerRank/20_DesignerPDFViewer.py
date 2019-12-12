'''
When you select a contiguous block of text in a PDF viewer, the selection is
highlighted with a blue rectangle. In this PDF viewer, each word is
highlighted ndependently.

In this challenge, you will be given a list of letter heights in the alphabet
and a string. Using the letter heights given, determine the area of the
rectangle highlight in mm^2 assuming all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are
t = 2, o = 1, r = 1 and n = 1. The tallest letter is 2 high and there are 4
letters. The hightlighted area will be 2 * 4 = 8 mm^2 so the answer is 8.

The first line contains 26 space-separated integers describing the respective
heights of each consecutive lowercase English letter, ascii[a-z].
The second line contains a single word, consisting of lowercase English
alphabetic letters.

Output Format
Print a single integer denoting the area in mm^2 of highlighted rectangle when
the given word is selected. Do not print units of measure.

Sample Input 0
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output 0
9

Explanation 0
We are highlighting the word abc:
Letter heights are a = 1, b = 3 and c = 1. The tallest letter, b, is 3 mm high.
The selection area for this word is 3 * 1mm * 3mm = 9mm^2.

Note: Recall that the width of each character is 1mm.

Sample Input 1
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

Sample Output 1
28

Explanation 1
The tallest letter in zaba is z at 7mm. The selection area for this word is
4 * 1mm * 7mm = 28mm^2.
'''


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    return max([h[ord(i) - 97] for i in word]) * len(word)


def designerPdfViewer2(h, word):
    alpabet = list('abcdefghijklmnopqrstuvwxyz')
    result = 0
    i = 0
    max_height = 0
    for w in word:
        for i in range(len(alpabet)):
            if w == alpabet[i]:
                max_height = max(max_height, h[i])
    result = max_height * len(word)
    return(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # h = list(map(int, input().rstrip().split()))
    # word = input()

    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5]
    word = 'abc'
    result = designerPdfViewer(h, word)
    print(result)  # 9

    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 7]
    word = 'zaba'
    result = designerPdfViewer(h, word)
    print(result)  #28

    # fptr.write(str(result) + '\n')
    # fptr.close()
