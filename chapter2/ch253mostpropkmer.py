'''
Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.

Input: A string Text, an integer k, and a 4 × k matrix Profile.
Output: A Profile-most probable k-mer in Text.
'''

text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
k = 5
prof_matrix = [
    [0.2, 0.2, 0.3, 0.2, 0.3],
    [0.4, 0.3, 0.1, 0.5, 0.1],
    [0.3, 0.3, 0.5, 0.2, 0.4],    
    [0.1, 0.2 ,0.1, 0.1, 0.2]
]


def most_prop_kmer(text, k, prof_matrix):
    patterns = []
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
    
    def max_value(prob_map):
        max_v = 0
        for value in prob_map.values():
            if value > max_v:
                max_v = value
        return max_v

    for p in prob_map:
        if prob_map[p] == max_value(prob_map) and patterns == []:
            patterns.append(p)
            
    return patterns

    


