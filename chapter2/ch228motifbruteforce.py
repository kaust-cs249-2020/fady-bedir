from neighborhood import neighbors
from hammingdistance import hum_dist

file = open('/users/fadygamal/motif.txt', 'r')
text = file.read()
lines = text.split('\n')

#inputs
texts = lines[1:7]
k = 5
d = 2


'''
check whether a pattern is a substring of a string "text" with at most "d" mismatches
'''
def substring_mismatch_check(pattern, text, d):
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i : i + len(pattern)]
        if hum_dist(substring, pattern) <= d:
            return True
    return False

'''
given a collection of strings, we find is there's a pattern of length k repeated in all strings 
with at most d mismatches
'''

def enummerate_motif(texts, k, d):
    plist = []
    for i in range(len(texts[0]) - k + 1):
        patt = texts[0][i: i + k]
        neighs = neighbors(patt, d)
        for n in neighs:
            count = 0
            for t in texts:
                if substring_mismatch_check(n, t, d):
                    count += 1
            if count == len(texts):
                plist.append(n)
    patterns = list(dict.fromkeys(plist))
    return patterns

motif = enummerate_motif(texts, k, d)
motifstring = " ".join(motif)
print(motifstring)


        