from time import time
t1 = time()

from better_deB_graph import bruij
from eulepath import adjacentlist_to_graph
from eulepath import eulePath
from genomepath import pathtogenome

file = open('/users/fadygamal/Desktop/solvecode/construct.txt', 'r')
data = file.read()
lines = data.split('\n')
kmers = lines[1:-1]

def reconstruct_string(kmers):
    debruGraph = bruij(kmers)
    graph = adjacentlist_to_graph(debruGraph)
    path = eulePath(graph)
    genome = pathtogenome(path)
    return genome

genome = reconstruct_string(kmers)
file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(genome)
file.close()

t2 = time()
print(t2 - t1)