'''
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.

Input: An amino acid string Peptide and a collection of integers Spectrum.
Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
'''

from ch445cyclicspectrum import cyclicSpectrum
from ch465cyclopeptideSequencing import digitize_spectrum

file = open('/users/fadygamal/Desktop/solvecode/cyclopeptidescore.txt', 'r')
data = file.read()
lines = data.split('\n')

peptide = lines[0]
#print(peptide)
spectrum = lines[1]
#print(spectrum)
spectrum = digitize_spectrum(spectrum.split())
#print(spectrum)

def cyclopep_score(peptide, spectrum):
    pep_spectrum = cyclicSpectrum(peptide)
    #print(pep_spectrum)
    s = spectrum.copy()
    count = 0
    for mass in pep_spectrum:
        if mass in s:
            count += 1
            s.remove(mass)
    return count

#score = cyclopep_score(peptide, spectrum)
#print(score)