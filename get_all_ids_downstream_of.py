import networkx as nx
import itertools
import sys
import os

start_node = sys.argv[1]
os.system("cat lib/x* > lib/taxdump/nodes.dmp")


G = nx.DiGraph()

with open("lib/taxdump/nodes.dmp", "r") as data:
    for line in data.readlines():
        cols = line.split("\t|\t")
        G.add_edge(cols[1], cols[0])




for i in set(itertools.chain.from_iterable(nx.dfs_edges(G,source=start_node))):
    print i







