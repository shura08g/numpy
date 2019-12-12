def calc_hash(data):
    k = 3571
    s = 0
    i = 1
    data += 84832941
    while data > 0:
        s += data % 2 * k ** i
        i += 1
        data //= 2
    return s % 2 ** 32  # 32 bit hash
    # return s % 2 ** 64  # 64 bit hash
    # return s % 2 ** 128  # 32 bit hash


for x in range(11):
    print("Hash {0}: {1}".format(x, calc_hash(x)))

for x in [1000, 1001, 1002, 1003, 1004, 1005]:
    print("Hash {0}: {1}".format(x, calc_hash(x)))

for x in [1701634284, 17016342840, 1701634284489749448987489]:
    print("Hash {0}: {1}".format(x, calc_hash(x)))

print(len("3634951947"))  # 10
print(len("2509012871680854964"))  # 19
print(len("136462872261723111245381832957875151120"))  # 39
