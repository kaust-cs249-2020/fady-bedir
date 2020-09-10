'''
review ham distance, neighborhood and apply miss match patterns function 

'''
text = 'ATGCCCAGAGATGAGGAAGTAGTAGGACCCATGCCCATGCCCAGTAGAGTGAGAATGAGTAGTAGTAGAGTAGAGTCCCCCCAGGAATGATGGAATGGAAGTGAAGTATGAGTAGGAAGTGAAGTGAATGATGAGGAGAAGTCCCGAGAAGTGAAGTAGTAGTGAAGTATGATGATGATGAGCCCGACCCAGCCCATGAGAGTCCCATGAGTAGAGAG'
k = 5
d = 2

def ham_dist(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count

def neighborhood(pattern, d):
    nucleotides = ["A", "C", "G", "T"]
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return nucleotides
    hood = []
    suffixpattern = neighborhood(pattern[1:], d)
    for txt in suffixpattern:
        if ham_dist(pattern[1:], txt) < d:
            for n in nucleotides:
                hood.append(n + txt)
        else:
            hood.append(pattern[0] + txt)
    return hood

def freq_patt_w_mis(text, k, d):
    patterns = []
    freq_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        neighbors = neighborhood(pattern, d)
        for j in range(len(neighbors)):
            neighbor = neighbors[j]
            if neighbor not in freq_map:
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1

    def maxmap(freq_map):
        maxvalue = 0
        for key, value in freq_map.items():
            if value > maxvalue:
                maxvalue = value
        return maxvalue

    m = maxmap(freq_map)
    for neighbor in freq_map:
        if freq_map[neighbor] == m:
            patterns.append(neighbor)
    return patterns

    
from reversecomplement import rev_string

textrev= rev_string(text)
alltext = text + textrev

freq_words_w_mis_rev = freq_patt_w_mis(textrev, k, d)

freq_words_w_mis = freq_patt_w_mis(alltext, k, d)


all_patterns = freq_words_w_mis + freq_words_w_mis_rev
print(freq_words_w_mis)


'''
def words_w_mis_rev(patterns1, patterns2):
    out = []
    for i in range(len(patterns1)):
        if patterns1[i] in patterns2:
            out.append(patterns1[i])
    return out

print (words_w_mis_rev(freq_words_w_mis_rev, freq_words_w_mis))
'''