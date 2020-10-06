'''
string Composition Problem: Generate the k-mer composition of a string.

Input: An integer k and a string Text.
Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.
'''

file = open('/users/fadygamal/compo.txt', 'r')
data = file.read()
lines = data.split('\n')


k = int(lines[0])
text = lines[1]


def kmer_composition(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        kmers.append(kmer)
        #kmers.sort()
    return kmers

'''output = kmer_composition(text, k)
output_format = "\n".join(output)

file = open('/users/fadygamal/Desktop/out.txt', 'w')
file.write(output_format)
file.close'''
