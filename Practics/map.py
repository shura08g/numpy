import math


def area(radius):
    return math.pi * (radius**2)

radii = [2, 5, 6, 8.5, 11, 20.5]

# areas = []
# for x in radii:
#     areas.append(area(x))
# print(areas)
ar2 = list(map(area, radii))
print(ar2)

temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19),
         ('LosAngeles', 26), ('Tokio', 27), ('New York', 28),
         ('London', 22), ('Kyiv', 18)]

# c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)


def c_to_f(data):
    return (data[0], (9 / 5) * data[1] + 32)

temp_in_f = list(map(c_to_f, temps))

print(temp_in_f)
