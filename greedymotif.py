'''
Implement GreedyMotifSearch.

Input: Integers k and t, followed by a collection of strings Dna.
Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
'''
from motifmatrix import prof_matrix
from motifmatrix import score
from motifmatrix import motif_to_matrix
from mostpropkmer import most_prop_kmer

file = open('/users/fadygamal/greedy.txt', 'r')
text = file.read()
lines = text.split('\n')


k = 12
t = 25
dna = lines[1:]

def greeddymotif(k, t, dna): 
    bestmotifs = []                     #list of the first k-mers in each string of collection dna
    for text in dna:
        bestmotif = [text[:k]]
        bestmotifs.append(bestmotif)
    
    for i in range (len(dna[0]) - k + 1): #iterate through each k pattern in the first string in dna
        motif = [dna[0][i : i + k]]
        motifs = [motif]                  #to form lists in a big list = matrix

        for j in range(1, t):                   #iterate through each other string in dna to
            profile = prof_matrix(motifs, k)    #form a probability profile form the motifs matrix above
            motifs.append(most_prop_kmer(dna[j], k, profile))   #then get a most probable kmer and add it to the motifs above                                                       
        
        scored_best_motifs = score(bestmotifs, k)   # compare scores between motifs from the first dna string
        scored_motifs = score(motifs, k)            # and motifs collected from each strand and take the one with
        if scored_motifs[0] < scored_best_motifs [0]:   # the smallest score
            bestmotifs = motifs
    
    onelist = []                    #empty the matrix into one big list of strings 
    for item in bestmotifs:
        onelist.append(item[0])
    
    return " ".join(onelist)        # to return the output as strings and not a list



print(greeddymotif(k, t, dna))