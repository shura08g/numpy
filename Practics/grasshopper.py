"""
    Кузнечик может прыгать на 1 и 2 клетки.
    Сколько различных траэкторий допригать из 1 до N?
    Kn = Kn-2 + Kn-1
"""


def traj_num(N):
    K = [0, 1] + [0] * (N - 1)
    for i in range(2, N + 1):
        K[i] = K[i - 2] + K[i - 1]
    return K[N]


print(traj_num(6))


"""
    Возможны ходы +1, +2, +3
    Если не все клетки доступны
"""


def count_trajectories(N: int, allowed: list):
    K = [0, 1, int(allowed[2])] + [0] * (N - 2)
    for i in range(3, N + 1):
        if allowed[i]:
            K[i] = K[i - 1] + K[i - 2] + K[i - 3]
    return K[N]

N = 10
lst1 = list(range(N + 1))
print(lst1)
lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst3 = [0, 1, 2, 0, 4, 5, 6, 7, 0, 9, 10]
print(count_trajectories(N, lst1))
print(count_trajectories(N, lst2))
print(count_trajectories(N, lst3))


"""
    Минимальная стоимость достижения клетки N
    price[i] - цена за посещение клетки i
    C[i] - (cost) ьинимальная скорость достижения клетки i
"""


def count_min_cost(N: int, price: list):
    # float("-inf") - бесконечность
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (N - 2)
    for i in range(3, N + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[N]

print("Min cost:", count_min_cost(N, lst1))
