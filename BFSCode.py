import numpy as np


def create_empty_graph(size):
    new_graph = np.zeros((size, size), dtype=int)
    return new_graph



def add_edge(graph, v1, v2):
    graph[v1, v2] = 1
    graph[v2, v1] = 1
    return graph


def remove_edge(graph, v1, v2):
    graph[v1, v2] = 0
    graph[v2, v1] = 0
    return graph


def mat_to_dictionary(mat):
    number_rows = np.shape(mat)[0]
    number_columns = np.shape(mat)[1]
    adjlist_dictionary = {}
    for i in range(number_rows):
        adjlist_dictionary[i] = []
    for j in range(0, number_rows):
        for i in range(0, number_columns):
            if mat[j][i] == 1:
                adjlist_dictionary[i].append(j)
    return adjlist_dictionary


def BFS(adjacency_lists, s):
    number_of_nodes = len(adjacency_lists)
    colors = ['white'] * number_of_nodes
    distances = [-1] * number_of_nodes
    predecessors = [None] * number_of_nodes

    colors[s] = 'gray'
    distances[s] = 0

    queue = []

    queue.append(s)

    while(queue):
        u = queue.pop()
        for v in adjacency_lists[u]:
            if colors[v] == 'white':
                colors[v] = 'gray'
                distances[v] = distances[u] + 1
                predecessors[v] = u
                queue.append(v)
        colors[u] = 'black'

    return (distances, predecessors)


if __name__ == '__main__':
    graph = create_empty_graph(8)

    graph = add_edge(graph, 0, 1)
    graph = add_edge(graph, 0, 4)
    graph = add_edge(graph, 1, 5)
    graph = add_edge(graph, 2, 3)
    graph = add_edge(graph, 2, 5)
    graph = add_edge(graph, 2, 6)
    graph = add_edge(graph, 3, 6)
    graph = add_edge(graph, 3, 7)
    graph = add_edge(graph, 5, 6)
    graph = add_edge(graph, 6, 7)

    print("Matrix representation of the in put graph:")
    print(graph)
    graph = mat_to_dictionary(graph)

    print()
    print("Adjacency list representation of the in put graph:")
    for node in graph:
        print(graph[node])
    distances, predecessors = BFS(graph, 1)
    print()
    print("Distances:")
    print(distances)
    print()
    print("Predecessors:")
    print(predecessors)