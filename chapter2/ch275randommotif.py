from time import time
from random import randint

from motifmatrix import prof_matrix
from motifmatrix import score
from motifmatrix import motif_to_matrix
from mostpropkmer import most_prop_kmer
from laplacescoremat import laplace_score
from laplacescoremat import laplace_prof_matrix

t1 = time()


file = open('/users/fadygamal/rand.txt', 'r')
text = file.read()
lines = text.split('\n')

k = 15
t = 20
dna = lines[1:]
repeats = 2

def random_motif(dna, k, t):
    motifs = []
    for item in dna:
        n = randint(0, len(item) - k)
        motif = [item[n: n+k]]
        motifs.append(motif)
    
    bestmotifs = motifs

    while(True):
        profile = laplace_prof_matrix(motifs, k)
        motifs = []
        for each in dna:
            motifs.append(most_prop_kmer(each, k, profile))
        
        scored_motifs = score(motifs, k)
        scored_best_motifs = score(bestmotifs, k)
        if scored_motifs[0] < scored_best_motifs[0]:
            bestmotifs = motifs
        else:
            return bestmotifs


def iterate_rand_motif(dna, k, t, repeats):
    bestmotifs = random_motif(dna, k, t)
    i = 0
    while i < repeats:
        motifs = random_motif(dna, k, t)
        scored_motifs = score(motifs, k)
        scored_best_motifs = score(bestmotifs, k)
        if scored_motifs[0] < scored_best_motifs[0]:
            bestmotifs = motifs
        i += 1
    return bestmotifs, i

best_of_motifs = iterate_rand_motif(dna, k, t, repeats)
justmotifs = best_of_motifs[0]
confirm_repeat = best_of_motifs[1]

justmotifs_list = []
for item in justmotifs:
    justmotifs_list.append(item[0])

justmotifs_string = "\n".join(justmotifs_list)

print(justmotifs_string)
print(confirm_repeat)




file = open('/users/fadygamal/Desktop/out.txt', 'w')
file.write(justmotifs_string)
file.close

t2 = time()
print(t2 - t1)