import numpy as np
import networkx as nx
import random


def PRA(N,m):
    A = nx.Graph()
    A.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
    list_of_vertex = [1, 2, 3, 4, 5]

    for i in range(6,N):
        A.add_node(i)
        edge_list = []
        random_list = []
        ncounter = 0
        while ncounter < m:
            ran = random.choice(list_of_vertex)
            if ran not in random_list:
                random_list.append(ran)
                edge_list.append((i,ran))
                ncounter += 1

        A.add_edges_from(edge_list)
        list_of_vertex.append(i)

    return A


def BA(N, m):  # N number of vertex=time, m number of degree on each vertex
    # setup initial graph
    A = nx.Graph()
    # time evolve
    A.add_edges_from([(1, 2), (2, 3),(3,4),(4,5),(5,1)])

    list_of_vertex = [1,2,2,3,3,4,4,5,5,1]

    # add new node
    for i in range(6, N):
        A.add_node(i)
        edge_list = []
        random_list = []
        ncounter = 0
        while ncounter < m:
            ran = random.choice(list_of_vertex)
            if ran not in random_list:
                random_list.append(ran)
                edge_list.append((i,ran))
                ncounter += 1

        if len(edge_list) != m:
            raise Exception("too few edges created")
        A.add_edges_from(edge_list)
        for e in edge_list:
            list_of_vertex.append(e[0])
            list_of_vertex.append(e[1])

    return A


def degree_frequency(G):
    freq_list = nx.degree_histogram(G)
    normalise = np.array(freq_list) / float(G.number_of_nodes())
    return np.arange(len(freq_list)), normalise


def degree_to_logbin(G):
    return G.degree().values()


def av_k(G):
    arr = np.array(G.degree().values())
    return np.mean(arr)



