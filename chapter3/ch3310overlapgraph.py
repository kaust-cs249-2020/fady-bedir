'''Solve the Overlap Graph Problem (restated below).

Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. 
(You may return the nodes and their edges in any order.)'''



from time import time
t1 = time()

file = open('/users/fadygamal/Desktop/solvecode/overlap.txt', 'r')
data = file.read()
lines = data.split('\n')

patterns = lines
#print(patterns)


def overlap_graph(patterns):
    overlapGraph = []
    for i in range(len(patterns)):
        suffix1 = patterns[i][1:]
        rmv_ith_pattern = list(patterns)
        rmv_ith_pattern.remove(rmv_ith_pattern[i])
        for j in range(len(rmv_ith_pattern)):
            prefix2 = rmv_ith_pattern[j][:-1]
            if suffix1 == prefix2:
                overlapGraph.append(patterns[i]+' -> '+rmv_ith_pattern[j])
    return overlapGraph

output_format = "\n".join(overlap_graph(patterns))
print(output_format)
'''file = open('/users/fadygamal/Desktop/out.txt', 'w')
file.write(output_format)
file.close

t2 = time()
print(t2 - t1)'''