file = open("test.txt", 'r')

for i in range(11):
    print(str(i) + ' ' + file.read(8))

file.close()


test = print("TEST None")

if test is None:
    print("None")
else:
    print("NOT None")


fib = {1: 2, 2: 3, 3: 7, 4: 9, 7: 11}

print(fib.get(2, 0) + fib.get(7, 0) + fib.get(5, 10))

tupl = (1, (1, 2, 3))
for i in range(len(tupl)):
    print(tupl[i])

for i in range(len(tupl)):
    st = str(tupl[i])
    temp = []
    for i in st:
        try:
            if i.isdigit():
                temp.append(i)
        except:
            pass
    #  print(temp)
    for j in range(len(temp)):
        print(temp[j])

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("tuple size: " + str(t.__sizeof__()))
print("list size: " + str(lst.__sizeof__()))

a = 10
a = a/3
print(a)
