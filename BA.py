from __future__ import division
import numpy as np
import networkx as nx
import random
import bisect


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


def av_k(degree_data):
    arr = np.array(degree_data)
    return np.mean(arr)


def create_many(N,m,num=50,func=BA):
    all_val = None
    all_freq = None
    all_data = []
    max_k = []
    for i in range(num):
        G = func(N,m)
        val, freq = degree_frequency(G)
        data = degree_to_logbin(G)
        k1 = max(val)
        max_k.append(k1)
        all_data += data

        if all_val is None:
            all_val = val
        else:
            all_val = np.concatenate((all_val,val))

        if all_freq is None:
            all_freq = freq
        else:
            all_freq = np.concatenate((all_freq,freq))

    return all_data, all_val, all_freq, max_k


def derivative2nd(x):
    k = np.gradient(np.gradient(x,edge_order=2),edge_order=2)
    return k


def turning_pt(c,b, tol=0.4): #get rid of k<20 in the begining too
    if type(b) is list:
        b = np.array(b)
    data = np.log(b)
    ind_s = bisect.bisect(c,20)

    d = derivative2nd(data[ind_s:])
    diff = np.diff(d)
    diff = abs(diff)
    a = diff > tol
    a = list(a)
    ind_e = a.index(1) + ind_s
    return ind_s, ind_e


def BA_kdistr(k,m):
    return (2*m*(m+1))/(k*(k+1)*(k+2))


def PRA_kdistr(k,m):
    return (m**(k-m))/((m+1)**(k-m+1))


def get_k1(func_name,N,m):
    if func_name == "PRA":
        return m - (np.log(N)/np.log(m/(m+1)))
    elif func_name == "BA":
        return np.sqrt(0.25+N*m*(m+1)) - 0.5
    else:
        raise Exception("wrong func name, need to be string")
