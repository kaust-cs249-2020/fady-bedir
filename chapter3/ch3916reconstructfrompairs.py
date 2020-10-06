from time import time
t1 = time()

from eulepath import eulePath
from reconstructpairspath import gen_from_pairs


file = open('/users/fadygamal/Desktop/solvecode/stringfrompairs.txt', 'r')
pairs = file.read()
pairs = pairs.split('\n')
k= 50
d= 200

def reformat(pairs):
    out = []
    for item in pairs:
        e = item.split('|')
        out.append(e)
    return out

pairs = reformat(pairs)
#print(pairs)

def bruij_pairs(pairs):
    bruij_adj_list = {}
    for pair in pairs:
        read1 = pair[0]
        read2 = pair[1]
        prefix = (read1[:-1], read2[:-1])
        suffix = (read1[1:], read2[1:])
        if prefix not in bruij_adj_list:
            bruij_adj_list[prefix] = [suffix]
        else:
            bruij_adj_list[prefix].append(suffix)
    return bruij_adj_list

def reconstruct_pairs(pairs, k, d): 
    adj_list = bruij_pairs(pairs)
    #print(adj_list)
    path = eulePath(adj_list)
    #print(path)
    gen = gen_from_pairs(path, k, d)
    #print(gen)
    return gen

genomefrompairs = reconstruct_pairs(pairs, k, d) 
print(genomefrompairs)

t2 =  time()
print(t2 - t1)