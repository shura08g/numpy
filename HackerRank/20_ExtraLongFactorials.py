'''
The factorial of the integer n, written n!, is defined as:
n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

Calculate and print the factorial of a given integer.

For example, if n = 30, we calculate 30 * 29 * 28 * ... * 2 * 1 and get
265252859812191058636308480000000.

Function Description
Complete the extraLongFactorials function in the editor below. It should print
the result and return.

extraLongFactorials has the following parameter(s):
n: an integer

Note: Factorials of n > 20 can't be stored even in a 64 - bit long long
variable. Big integers must be used for such calculations. Languages like Java,
Python, Ruby etc. can handle big integers, but we need to write additional code
in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

Input Format
Input consists of a single integer n


Output Format
Print the factorial of n.

Sample Input
25

Sample Output
15511210043330985984000000
'''


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = 1
    if n <= 1:
        result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)


if __name__ == '__main__':
    # n = int(input())
    n = 30
    extraLongFactorials(n)  # 265252859812191058636308480000000

    n = 25
    extraLongFactorials(n)  # 15511210043330985984000000
