from ch4112theoriticalspectrum import prefix_mass_array

peptide = 'ITFYAMTDGALTHPQ'

def cyclicSpectrum(peptide): #a function to build a list of the cyclic masses spectrum  of the cyclic peptide

    prefix_mass = prefix_mass_array(peptide) #get the list of the masses of each prefix in the peptide
    peptide_mass = prefix_mass[len(peptide)] #get the mass of the whole peptide
    cycSpec = [0]                            #set an empty list to store the spectrum
    for i in range(len(peptide)):            #iterate through each aa in the peptide
        for j in range(i+1, len(peptide)+1):    #iterate through each prefix in peptide prefix mass list
            cycSpec.append(prefix_mass[j] - prefix_mass[i]) #substract the mass of the prefix ending at each of the remaining aa in the peptide
                                                            #from the mass of the prefix ending at the aa (i) and add it to the spec list
            if i > 0 and j < len(peptide):  #to get the mass of prefix spanning the ends of the cyclic peptide
                cycSpec.append(peptide_mass - (prefix_mass[j] - prefix_mass[i])) #substract the mass of the current substring 
    return sorted(cycSpec)                                                       #from the mass of the whole peptide and add it to the cyclic spectrum list

'''out = cyclicSpectrum(peptide)

outstr = " ".join(str(i) for i in out)
print(outstr)'''