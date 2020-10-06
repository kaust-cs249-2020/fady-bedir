'''
The following pseudocode assumes that we have a string or list of symbols Alphabet containing
the 20 symbols of the amino acid alphabet, and a dictionary AminoAcidMass whose keys are the symbols of 
Alphabet and whose values are the the integer masses of each symbol.

LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass[s]
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    return sorted list LinearSpectrum
'''
file = open('/users/fadygamal/Desktop/solvecode/integer_mass_table.txt', 'r')
data = file.read()
lines = data.split('\n')

def int_mass_dict(lines):       #a function to turn the integer mass table into a dict
    mass_dict = {}             #start with an empty dict to store the keys and values
    for item in lines:          #for every string in the lines of the table file provided
        aa = item[0]            #the aa is the first letter of the string
        mass = int(item[2:])               #the corresponding mass is the number after the space
        if aa not in mass_dict: #start adding the aa as keys in the empty dict
            mass_dict[aa] = mass      #and set the values as their corresponding mass
    return mass_dict           #output the mass table dict

intmassdict = int_mass_dict(lines)
aminos = list(intmassdict.keys())
peptide = 'VKY'

def prefix_mass_array(peptide):  #a function to build a list of the masses of each prefix in the peptide
    prefix_mass = [0]                                               #start with an empty list
    for i in range(len(peptide)):                                   #iterate through each aa in the peptide          
        prefix_mass.append(prefix_mass[i] + intmassdict[peptide[i]])    #sum the mass of the current aa with the previous one (i in the list)
    return prefix_mass                                                  #and add it to the prefix masses list
#print(prefix_mass_array(peptide))
def LinearSpectrum(peptide):    #a function to build a list of the linear masses spectrum  of the peptide
    prefix_mass = prefix_mass_array(peptide)    #get the list of the masses of each prefix in the peptide
    linearspec = [0]                            #set an empty list to store the spectrum
    for i in range(len(peptide)):               #iterate through each aa in the peptide
        for j in range(i+1, len(peptide)+1):        #iterate through each prefix in the peptide prefix mass list
            linearspec.append(prefix_mass[j] - prefix_mass[i]) #substract the mass of the prefix ending at each of the remaining aa in the peptide
    return sorted(linearspec)                                  #from the mass of the prefix ending at the aa (i) and add it to the spec list

#out = LinearSpectrum(peptide)

#outstr = " ".join(str(i) for i in out)
#print(outstr)

