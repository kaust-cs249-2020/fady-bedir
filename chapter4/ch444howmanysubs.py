'''
Exercise Break: How many subpeptides does a cyclic peptide of length n have?
'''

def count_subpeps(cyc_peptide_length):
    n = peptide_length
    return n * (n-1)

subpepsCount = count_subpeps(31315)
#print(subpepsCount)