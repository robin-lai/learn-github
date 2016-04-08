from random import shuffle
from utils import myparse_karate
"""
learn implimetation of pagerank
"""
def pagerank(graph, n_iter):
    n_node = len(graph)
    print(n_node)
    nodes = [i for i in range(n_node)]
    pr = [1/n_node for i in range(n_node)]
    shuffle(nodes)

    while n_iter:
        for node in nodes:
            for neigh in graph[node]:
                pr[node] += pr[neigh]/len(graph[neigh])

        print(n_iter,':',pr,end=' ')
        print()
        n_iter = n_iter - 1

graph_karate = myparse_karate('Data/karate.csv',True)
pagerank(graph_karate,10)
#graph_dict = {0:[1,2,3,4,5,6,7,8,9],1:[0],2:[0],3:[0],4:[0],5:[0],6:[0],7:[0],8:[0],9:[0]}
#pagerank(graph_dict, 10)

