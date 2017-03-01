import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random


def generate_BA(N, m):  # N number of vertex=time, m number of degree on each vertex
    # setup initial graph
    G = nx.Graph()
    # time evolve
    for i in range(m+1):
        G.add_node(i)
    list_of_vertex = []
    for s in range(m+1):
        for t in range(s + 1, m+1):
            G.add_edge(s, t)
            print '--- new edge from', s, ' to ', t  # useful for debugging

    # Add linked existing vertex to list
    for i in G.edges():
        list_of_vertex.append(i[0])
        list_of_vertex.append(i[1])

    # add new node
    for i in range(m + 1, N + 1):
        G.add_node(i)
        edge_list = []
        for n in range(m):
            edge_list.append((i, random.choice(list_of_vertex)))
        G.add_edges_from(edge_list)
        for e in edge_list:
            list_of_vertex.append(e[0])
            list_of_vertex.append(e[1])
    return G


def degree_frequency(G):
    freq_list = nx.degree_histogram(G)
    normalise = np.array(freq_list) / float((len(G) - 1))
    return np.arange(len(freq_list)), normalise


def degree_to_logbin(G):
    return G.degree().values()


def av_k(G):
    arr = np.array(G.degree().values())
    return np.mean(arr)


if __name__ == "__main__":
    G = generate_BA(20, 2)
    nx.draw(G)
    plt.show()
