import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict

def myparse_karate(filename, isDirected):
    graph_karate = {}
    reader = list(csv.reader(open(filename)))
    for row in reader:
        src = int(row[0])-1
        dest = int(row[2])-1
        if src not in graph_karate:
            graph_karate[src]=[]
        if dest not in graph_karate:
            graph_karate[dest]=[]
        graph_karate[src].append(dest)
    print(graph_karate)
    return graph_karate

myparse_karate('Data/karate.csv',True)

def parse(filename, isDirected):
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in reader]

    print("Reading and parsing the data into memory...")
    if isDirected:
        return parse_directed(data)
    else:
        return parse_undirected(data)

def parse_undirected(data):
    G = nx.Graph()
    nodes = set([row[0] for row in data])
    edges = [(row[0], row[2]) for row in data]

    num_nodes = len(nodes)
    rank = 1/float(num_nodes)
    G.add_nodes_from(nodes, rank=rank)
    G.add_edges_from(edges)

    return G

def parse_directed(data):
    DG = nx.DiGraph()

    for i, row in enumerate(data):

        node_a = format_key(row[0])
        node_b = format_key(row[2])
        val_a = digits(row[1])
        val_b = digits(row[3])

        DG.add_edge(node_a, node_b)
        if val_a >= val_b:
            DG.add_path([node_a, node_b])
        else:
            DG.add_path([node_b, node_a])

    return DG

def digits(val):
    return int(re.sub("\D", "", val))

def format_key(key):
    key = key.strip() 
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key 


def print_results(f, method, results):
    print(method)

