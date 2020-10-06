'''
We say that a DNA string Pattern encodes an amino acid string Peptide 
if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide. 
For example, the DNA string GAAACT is transcribed into GAAACU and translated into ET. 
The reverse complement of this DNA string, AGTTTC, is transcribed into AGUUUC and translated into SF. 
Thus, GAAACT encodes both ET and SF.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
Output: All substrings of Text encoding Peptide (if any such substrings exist).
'''
from time import time
t1 = time()

from ch423proteintranslation import codon_dict
from ch423proteintranslation import translate_RNA
from reversecomplement import rev_string

file = open('/users/fadygamal/Desktop/solvecode/codontable.txt', 'r')
data = file.read()
lines = data.split('\n')
codonTable = codon_dict(lines)
file2 = open('/users/fadygamal/Desktop/solvecode/Bacillus_brevis.txt', 'r')
data2 = file2.read()
lines2 = data2.split('\n')
lines2 = ''.join(lines2)

DNA = lines2
#print(DNA)
peptide = 'VKLFPWFNQY'

def RNA_transcription(DNA):
    RNA = ''
    for i in range(len(DNA)):
        if DNA[i] == 'T':
            RNA += 'U'
        else:
            RNA += DNA[i]
    return RNA
#RNA = RNA_transcription(DNA)
#print(RNA)

def reverse_transcribe(RNA):
    DNA = ''
    for i in range(len(RNA)):
        if RNA[i] == 'U':
            DNA += 'T'
        else:
            DNA += RNA[i]
    return DNA


def peptide_encoding(DNA, peptide, codonTable):
    substrings = []                     #start with an empty list
    k = len(peptide)*3                  #get the length of the DNA substring encoding for the peptide
    for i in range(len(DNA) - k):       #iterate the DNA string
        kmer = DNA[i: i +k]                                                       #take every substring of the determined lenght
        kmer_transcribed = RNA_transcription(kmer)                                #transcribe it to RNA
        kmer_translated = translate_RNA(codonTable, kmer_transcribed)             #translate it to peptides 
        revkmer = rev_string(kmer)                                                #also get the revverse complement of the the substring 
        revkmer_transcribed = RNA_transcription(revkmer)                          #transcribe it to RNA
        revkmer_translated = translate_RNA(codonTable, revkmer_transcribed)       #translate it to peptides
        if kmer_translated == peptide or revkmer_translated == peptide:           #check both peptides you created, if any of them are the same as
            substrings.append(kmer)                                               #the peptide of interest, add the substring to the empty list 
    return substrings

substrings= peptide_encoding(DNA, peptide, codonTable)
print(substrings)

t2= time()
print(t2 - t1)