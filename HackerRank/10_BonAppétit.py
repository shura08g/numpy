'''
Anna and Brian are sharing a meal at a restuarant and they agree to split the
bill equally. Brian wants to order something that Anna is allergic to though,
and they agree that Anna won't pay for that item. Brian gets the check and
calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6]. Anna
declines to eat item k = [2] which costs 6. If Brian calculates the bill
correctly, Anna will pay (2 + 4) / 2 = 3. If he includes the cost of bill[2],
he will calculate (2 + 4 + 6) / 2 = 6. In the second case, he should refund
3 to Anna.

Input Format
The first line contains two space-separated integers n and k, the number of
items ordered and the 0-based index of the item that Anna did not eat.
The second line contains n space-separated integers bill[i] where 0 <= i <= n.
The third line contains an integer, b, the amount of money that Brian charged
Anna for her share of the bill.

Sample Input 0
4 1
3 10 2 9
12

Sample Output 0
5

Explanation 0
3 + 2 + 9 = 14
14 / 2 = 7
12 - 7 = 5

Sample Input 1
4 1
3 10 2 9
7

Sample Output 1
Bon Appetit

Explanation 1
3 + 2 + 9 = 14
14 / 2 = 7
7 - 7 = 0
'''


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum_ann = 0
    for i in range(len(bill)):
        if i != k:
            sum_ann += bill[i]
    result = b - (sum_ann // 2)
    if result == 0:
        print('Bon Appetit')
    else:
        print(result)


if __name__ == '__main__':
    # nk = input().rstrip().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # bill = list(map(int, input().rstrip().split()))
    # b = int(input().strip())

    n = 4
    k = 1
    bill = [3, 10, 2, 9]
    b = 12
    bonAppetit(bill, k, b)

    n = 4
    k = 1
    bill = [3, 10, 2, 9]
    b = 7
    bonAppetit(bill, k, b)
