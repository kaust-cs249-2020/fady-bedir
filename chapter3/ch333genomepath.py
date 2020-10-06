'''String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.

Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).'''

from time import time
t1 = time()
'''
file = open('/user''s/fadygamal/genpath.txt', 'r')
data = file.read()
lines = data.split('\n')


path = lines'''

def pathtogenome(path):
    kmer = path[0]
    k = len(kmer)
    endstring = kmer        
    list_no_first = path[1:]
    for j in range(len(list_no_first)):
        second = list_no_first[j][:-1]
        s = k-1
        check = endstring[j+1:s+j+1]
        if check == second:
            endstring += list_no_first[j][-1]
    
    return endstring

'''print(pathtogenome(path))

t2 = time()
print(t2 - t1)'''

