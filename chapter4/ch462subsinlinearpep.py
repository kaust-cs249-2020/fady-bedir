'''
Exercise Break: How many subpeptides does a linear peptide of given length n have? 
(Include the empty peptide and the entire peptide.)

Input: An integer n.
Output: The number of subpeptides of a linear peptide of length n.
'''

peptide_length = 37145

def count_subs_in_linerPep(peptide_length):
    sum = 0
    for i in range(peptide_length+1):
        sum += i
    return sum+1

print(count_subs_in_linerPep(peptide_length))