from time import time
import random

from motifmatrix import prof_matrix
from motifmatrix import score
from motifmatrix import motif_to_matrix
from mostpropkmer import most_prop_kmer
from laplacescoremat import laplace_score
from laplacescoremat import laplace_prof_matrix

from time import time
t1 = time()


file = open('/users/fadygamal/gibbs.txt', 'r')
text = file.read()
lines = text.split('\n')

k = 15
t = 20
n = 2000
dna = lines[1:]
repeats = 20

def prof_random_kmer(text, k, prof_matrix):

    prob_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        prob_pattern = 1
        for j in range(len(pattern)):
            p = pattern[j]
            if p == "A":
                prob_pattern = prob_pattern * prof_matrix[0][j]
            elif p == "C":
                prob_pattern = prob_pattern * prof_matrix[1][j]
            elif p == "G":
                prob_pattern = prob_pattern * prof_matrix[2][j]
            else:
                prob_pattern = prob_pattern * prof_matrix[3][j]

        if pattern not in prob_map:
            prob_map[pattern] = prob_pattern

    i = random.uniform(0, sum(list(prob_map.values())))
    c = 0
    for key, value in prob_map.items():
        c+= value
        if i <= c:
            return [key]

def gibbs_sampler(dna, k, t, n):

    motifs = []
    for item in dna:
        z = random.randint(0, len(item) - k)
        motif = [item[z: z+k]]
        motifs.append(motif)
    bestmotifs = motifs
    
    for number in range(n):
        i = random.randrange(t)
        motifs_xpt_i = motifs[:i] + motifs[i+1:]

        profile = laplace_prof_matrix(motifs_xpt_i, k)
        motifs[i] = prof_random_kmer(dna[i], k, profile)
        scored_motifs = laplace_score(motifs, k)
        scored_best_motifs = laplace_score(bestmotifs, k)
    
        if scored_motifs[0] < scored_best_motifs[0]:
            bestmotifs = motifs 
    
    return bestmotifs

def iterate_gibbs(dna, k, t, n, repeats):
    bestmotifs = gibbs_sampler(dna, k, t, n)
    i = 0
    while i < repeats:
        motifs = gibbs_sampler(dna, k, t, n)
        scored_motifs = laplace_score(motifs, k)
        scored_best_motifs = laplace_score(bestmotifs, k)

        if scored_motifs[0] < scored_best_motifs[0]:
            bestmotifs = motifs
        i += 1
    return bestmotifs, i

best_of_motifs = iterate_gibbs(dna, k, t, n, repeats)
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

