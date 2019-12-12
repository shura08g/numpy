from collections import deque


def bfs(vertex, G, used=None):
    '''
    обход в ширину (BFS - Breadth first search)
    '''
    pass

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

# кратчайший путь
parents = [None] * N
while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:
            distance[neigh_v] = distance[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print(path[::-1])
