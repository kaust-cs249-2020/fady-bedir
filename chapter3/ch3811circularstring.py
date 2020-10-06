from time import time
t1 = time()

from probability import generate_all
from better_deB_graph import bruij
from eulecycle import adjacentlist_to_graph
from eulecycle import euleCycle
from hammingdistance import hum_dist
from genomepath import pathtogenome

alphabet = '01'
k = 8

def circular_string(alphabet, k):

    kmers = generate_all(alphabet, k)
    deB = bruij(kmers)
    graph = adjacentlist_to_graph(deB)
    cycle = euleCycle(graph)
    cycle = cycle[:-(k-1)]
    genome = pathtogenome(cycle)    
    return genome

string = circular_string(alphabet, k)

file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(string)
file.close()

t2 = time()
print("finish after " + str(t2-t1))