
from ch4112theoriticalspectrum import LinearSpectrum, int_mass_dict
from ch445cyclicspectrum import cyclicSpectrum

file = open('/users/fadygamal/Desktop/solvecode/integer_mass_table_18.txt', 'r')
data = file.read()
lines = data.split('\n')
'''
def int_mass_dict(lines):       #a function to turn the integer mass table into a dict
    mass_dict = {}             #start with an empty dict to store the keys and values
    for item in lines:          #for every string in the lines of the table file provided
        aa = item[0]            #the aa is the first letter of the string
        mass = int(item[2:])               #the corresponding mass is the number after the space
        if mass not in mass_dict: #start adding the masses as keys in the empty dict
            mass_dict[mass] = [aa]      #and set the values as a list of their corresponding aa
        else:
            mass_dict[mass].append(aa)
    return mass_dict           #output the mass table dict'''
massTable = int_mass_dict(lines)
#print(massTable)

Spectrum = '0 71 99 101 101 113 115 128 128 129 137 200 200 208 214 228 228 229 229 243 265 299 313 329 329 336 337 344 356 357 366 400 428 436 437 442 457 457 465 472 494 513 537 556 557 558 564 565 566 585 609 628 650 657 665 665 680 685 686 694 722 756 765 766 778 785 786 793 793 809 823 857 879 893 893 894 894 908 914 922 922 985 993 994 994 1007 1009 1021 1021 1023 1051 1122'
Spectrum = Spectrum.split(' ')

def digitize_spectrum(Spectrum): #a function to reformat the spectrum as a list of integers
    digital = []
    for i in Spectrum:
        digital.append(int(i))
    return digital
Spectrum = digitize_spectrum(Spectrum)
#print(Spectrum)

def peptide_to_masses(peptide):  #a function to output the peptides found as a list of their masses
    num = []
    for aa in peptide:
        num.append(str(massTable[aa]))
    return '-'.join(num)

def Expand(peptides):           #a function to expand a peptide with each possible amino acid of the 18 mass table
    expanded_peptides = []                  #empty list to store the expanded peptides
    aminos = list(massTable.keys())         #make a list of all 18 amino acids
    for item in aminos:                     #take each amino acid
        for peptide in peptides:                #and each peptide in the list
            peptide += item                     #add the amino acid to the end of the peptide
            expanded_peptides.append(peptide)   #add the expanded peptide to the empty list
    return expanded_peptides                #output the list of expanded peptides
#print(Expand(['']))

def Mass(peptide):             #a function to calculate the mass of a peptide
    mass = 0
    for aa in peptide:
        mass += massTable[aa]
    return mass
#print(Mass(peptide))

def CyclopeptideSequencing(Spectrum):               #a function to obtain a cyclic peptide sequence from a given spectrum
    ParentMass = Spectrum[-1]                  #get the largest mass in the spectrum
    CandidatePeptides = ['']                        #a list to store peptides to test against the spectrum
    FinalPeptides = []                              #a list to store the peptides matching the spectrum
    FinalPeptidesMasses = []                        #a list to store the aa masses of peptides mathcing the spectrum 
    
    while len(CandidatePeptides) > 0:               #as long as the candidates list is not empty
        CandidatePeptides = Expand(CandidatePeptides)       #expand each candidate peptide
        #print(CandidatePeptides)
        for peptide in CandidatePeptides[:]:                #then take each candidate peptide
            if Mass(peptide) == ParentMass and peptide not in FinalPeptides:     #if its mass is equal to largest mass and the peptide is not in the final list
                if cyclicSpectrum(peptide) == Spectrum:                             #and if its cyclic spetrum is the same as the spectrum
                    FinalPeptides.append(peptide)                                       #then add it to the final list 
                    FinalPeptidesMasses.append(peptide_to_masses(peptide))              #and add its masses to the masses list for the output
                CandidatePeptides.remove(peptide)                                   #then remove it from the candidates list
            elif not all(a in Spectrum for a in LinearSpectrum(peptide)):        #if its mass is not the largest, check its linear spectrum, if it's not a part of the given spectrum
                CandidatePeptides.remove(peptide)                                       #remove it from the candidates list
    return FinalPeptidesMasses                      #finally after all candidates have been removed, return the list 
                                                    #of masses of the final peptides that fulfill the spectrum 
FinalPeptides = CyclopeptideSequencing(Spectrum)
#print(" ".join(FinalPeptides))

