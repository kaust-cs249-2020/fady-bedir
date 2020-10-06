from time import time
t1 = time()


from kmercomposition import kmer_composition
from overlapgraph import overlap_graph

file = open('/users/fadygamal/test.txt', 'r')
data = file.read()
lines = data.split('\n')

text = 'TAATGCCATGGGATGTT'
k = 4

kmers = lines

def debru_graph(kmers):
    nodes = []
    
    firstnode = kmers[0][:-1]
    nodes.append(firstnode)
    middle_kmers = kmers[1:]
    for i in range(len(middle_kmers)):
        nodes.append(middle_kmers[i][:-1])
    lastnode = kmers[-1][1:]
    nodes.append(lastnode)

    nodesdict = {}
    for y in range(len(nodes) - 1):
        if nodes[y] not in nodesdict:
            nodesdict[nodes[y]] = nodes[y+1]
        else:
            nodesdict[nodes[y]] += ", "+nodes[y+1]
    output = []
    for key, value in nodesdict.items():
        output.append(key+" -> "+value) 

    output = "\n".join(output)
    return output
    
kdb_graph = debru_graph(kmers)   
file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(kdb_graph)
file.close()
   
t2 = time()

print(t2 - t1)

