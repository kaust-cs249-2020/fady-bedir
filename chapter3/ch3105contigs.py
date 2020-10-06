from genomepath import pathtogenome
from better_deB_graph import bruij
from eulecycle import adjacentlist_to_graph
from maxnonbranchpath import branches

file = open('/users/fadygamal/Desktop/solvecode/contigs.txt', 'r')
data = file.read()
lines = data.split('\n')

patterns = lines

def contigs(patterns):
    deBgraph = bruij(patterns)
    graph = adjacentlist_to_graph(deBgraph)
    maxnonbranch = branches(graph)

    contigs = []
    for path in maxnonbranch:
        contigs.append(pathtogenome(path))
    return contigs
    
contigs = contigs(patterns)
conts = ''
for c in contigs:
    conts += c+" "

print(conts)