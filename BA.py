import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random


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
            raise Exception("too less edges created")
        A.add_edges_from(edge_list)
        for e in edge_list:
            list_of_vertex.append(e[0])
            list_of_vertex.append(e[1])

    return A


def choose(list_of_nodes, list_of_ran):
    ran = random.choice(list_of_nodes)
    if ran not in list_of_ran:
        return ran
    else:
        choose(list_of_nodes, list_of_ran)

def generate_BA(N, m):  # N number of vertex=time, m number of degree on each vertex
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
        for n in range(m):
            ran = choose(list_of_vertex, random_list)
            random_list.append(ran)
            edge_list.append((i,ran))
        if len(edge_list) != m:
            raise Exception("too less edges created")
        A.add_edges_from(edge_list)
        for e in edge_list:
            list_of_vertex.append(e[0])
            list_of_vertex.append(e[1])

    return A


def generate_BA_Multi(N, m):  # N number of vertex=time, m number of degree on each vertex
    # setup initial graph
    G = nx.MultiGraph()
    # time evolve
    G.add_edges_from([(1, 2), (2, 3),(3,4),(4,5),(5,1)])

    list_of_vertex = [1,2,2,3,3,4,4,5,5,1]

    # Add linked existing vertex to list
    # for i in G.edges():
    #     list_of_vertex.append(i[0])
    #     list_of_vertex.append(i[1])

    # add new node
    for i in range(6, N + 1):
        G.add_node(i)
        edge_list = []
        #print edge_list
        for n in range(m):
            edge_list.append((i, random.choice(list_of_vertex)))
        if len(edge_list) != m:
            raise Exception("too less edge")
        #print edge_list
        G.add_edges_from(edge_list)
        for e in edge_list:
            list_of_vertex.append(e[0])
            list_of_vertex.append(e[1])
        #print list_of_vertex
    return G


def degree_frequency(G):
    freq_list = nx.degree_histogram(G)
    normalise = np.array(freq_list) / float((len(freq_list)-1))
    return np.arange(len(freq_list)), normalise


def degree_to_logbin(G):
    return G.degree().values()


def av_k(G):
    arr = np.array(G.degree().values())
    return np.mean(arr)


if __name__ == "__main__":
    G = generate_BA(2000, 2)
    # nx.draw(G)
    # plt.show()
