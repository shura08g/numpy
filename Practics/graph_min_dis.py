'''
Поиск кратчайшего пути алгоритмом Дейкстра
'''


def main():
    G = read_graph()
    start = input("С какой вершины начать?")
    while start not in G:
        start = input("Такой вершины в графе нет. " +
                      " С какой вершины начать?")
    shortest_distances = dijkstra(G, start)
    finish = input("К какой вершине построить путь?")
    while finish not in G:
        finish = input("Такой вершины в графе нет. " +
                       "К какой вершине построить путь?")
    shortest_path = reveal_shortest_path(G, start, finish, shortest_distances)


def read_graph(G):
    M = int(input())  # M - количествло ребер, далее строки "A B вес"
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G


def add_edge(G, b, a, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

if __name__ == "__main__":
    main()
