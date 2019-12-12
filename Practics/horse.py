'''
Шахматный конь
кратчайший путь от 'd4' до 'f7'
'''
from collections import deque

letters = 'abcdefgh'  # все буквы на доске
numbers = '12345678'  # все цифры на доске
graph = dict()
for l in letters:
    for n in numbers:
        graph[l + n] = set()

print(*graph)
'''
a1 a2 a3 a4 a5 a6 a7 a8
b1 b2 b3 b4 b5 b6 b7 b8
c1 c2 c3 c4 c5 c6 c7 c8
d1 d2 d3 d4 d5 d6 d7 d8
e1 e2 e3 e4 e5 e6 e7 e8
f1 f2 f3 f4 f5 f6 f7 f8
g1 g2 g3 g4 g5 g6 g7 g8
h1 h2 h3 h4 h5 h6 h7 h8
'''


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

# все возможные ходы коня
for i in range(len(letters)):
    for j in range(len(numbers)):
        v1 = letters[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < len(letters) and 0 <= j + 1 < len(numbers):
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i - 2 < len(letters) and 0 <= j + 1 < len(numbers):
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i + 1 < len(letters) and 0 <= j + 2 < len(numbers):
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)

        if 0 <= i - 1 < len(letters) and 0 <= j + 2 < len(numbers):
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

for k, v in graph.items():
    print(k, v)

distance = {v: None for v in graph}
parents = {v: None for v in graph}
start_vertex = 'd4'
end_vertex = 'f7'
distance[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print(path[::-1])
# ['d4', 'b5', 'd6', 'f7']
