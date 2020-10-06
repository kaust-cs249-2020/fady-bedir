'''
The following problem asks you to find the translation of an RNA string into an amino acid string.

Protein Translation Problem: Translate an RNA string into an amino acid string.

Input: An RNA string Pattern and the array GeneticCode.
Output: The translation of Pattern into an amino acid string Peptide.
'''

file = open('/users/fadygamal/Desktop/solvecode/codontable.txt', 'r')
data = file.read()
lines = data.split('\n')
#print(lines)
file2 = open('/users/fadygamal/Desktop/solvecode/rnaseq.txt', 'r')
data2 = file2.read()
lines2 = data2.split('\n')
RNA = lines2[0]
#print(RNA)

def codon_dict(lines):       #a function to turn the codon table into a dict
    codon_dict = {}             #start with an empty dict to store the keys and values
    for item in lines:          #for every string in the lines of codon table file provided
        codon = item[:3]            #the codon is the first 3 letters of the string
        aa = item[-1]               #the corresponding amino acid is the last letter in the string
        if aa == ' ':               #if there's no amino acid i.e. if it's a stop codon
            aa = 0                      #set the value of the amino acid variable to zero
        if codon not in codon_dict: #start adding the codon as keys in the empty dict
            codon_dict[codon] = aa      #and set the values as their corresponding amino acid 
    return codon_dict           #output the codon table dict

#codonTable = codon_dict(lines)
#print(codonTable)

def translate_RNA(codonTable, RNA):   #a function to translate an RNA sequence into an amino acid sequence using the codon table 
    peptide = ''                            #start with an empty string
    for i in range(0, len(RNA), 3):         #iterate through the amino acid sequence in steps of 3 positions
        codon = RNA[i:i+3]                      #set the codon as the 3 RNA nucleotides starting at the position selected
        if codonTable[codon] != 0:              #check the codon in the codon table, if it's not a stop codon
            peptide += codonTable[codon]            #add its value i.e. its amino acid to the peptide sequence
        else:                                   #if the codon is a stop codon, break the loop and stop translation
            break
    return peptide                          #output the amino acid string collected so far

#aminoAcidString = translate_RNA(codonTable, RNA)
#print(aminoAcidString)


        