def build_quadratic_function(a, b, c):
    """Returns the fubction f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)

print(f(0))  # -5
print(f(1))  # 0
print(f(2))  # 9

f_new = build_quadratic_function(3, 0, 1)(2)  # 3x^2+1 evaluated for x=2

print(f_new)  # 13

test = build_quadratic_function(-1, 4, 7)  # -x^2 + 4x + 7

print(test(0))  # 7
print(test(1))  # 10
print(test(2))  # 11
print(test(3))  # 10
