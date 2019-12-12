from collections import deque

# M, N = [int(x) for x in input().split()]
# '''
# матрица смежностей
# N -количество вершин
# M - количество ребер
# '''
# V = []  # список
# index = {}  # пустой словарь
# A = [[0] * N for i in range(N)]  # структура матрицы смежностей

# for i in range(N):
#     v1, v2 = input().split()
#     for v in v1, v2:
#         if v not in index:
#             V.append(v)
#             index[v] = len(V) - 1
#         v1_i = index[v1]
#         v2_i = index[v2]
#         A[v1_i][v2_i] = 1
#         A[v2_i][v1_i] = 1

# print(*A)

'''
справочник
N -количество вершин
'''
# N = [int(x) for x in input().split()]
N = int(input())
G = {}

for i in range(N):
    v1, v2 = input().split()
    for v, u in (v1, v2), (v2, v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)

for k, v in G.items():
    print(k + ": " + str(v))


# 3
# 1 2
# 2 3
# 3 3
# 1: {'2'}
# 2: {'3', '1'}
# 3: {'3', '2'}

'''
компактное хранение списка смежностей
для неизменяемого графа
'''
edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
# ofset[i] - начало списка смежностей i-й вершины
offset = [0, 1, 4, 6, 9, 10]
# список смежностей лежит
# edges[offset[i]:offset[i + 1]]
for i in range(len(offset) - 1):
    print(edges[offset[i]:offset[i + 1]])

# [1]
# [0, 2, 3]
# [1, 3]
# [1, 2, 4]
# [3]


def dfs(vertex, G, used=None):
    '''
    обход в глубину (DFS - deep first search)
    '''
    used = used or set()
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

'''
Алгоритм Косарайю
'''


def bfs(vertex, G, used=None):
    '''
    обход в ширину (BFS - Breadth first search)
    '''

N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

distance = [None] * N
start_vertex = 0
distance[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            queue.append(neigh_v)
