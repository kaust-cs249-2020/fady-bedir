from time import time
t1 = time()
'''
file = open('/users/fadygamal/debru.txt', 'r')
data = file.read()
lines = data.split('\n')

kmers = lines'''

def bruij(kmers):
    nodes = []
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        nodes.append([prefix, suffix])

    nodesdict = {}
    for i in range(len(nodes)):
        if nodes[i][0] not in nodesdict:
            nodesdict[nodes[i][0]] = nodes[i][1]
        else:
            nodesdict[nodes[i][0]] += ","+nodes[i][1]
    output = []
    for key, value in nodesdict.items():
        output.append(key+" -> "+value) 

    #output = "\n".join(output)
    return output

'''kdb_graph = bruij(kmers)   
file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(kdb_graph)
file.close()


t2 = time()
print(t2 - t1)'''