'''
Trim(Leaderboard, Spectrum, N, Alphabet, AminoAcidMass)
    for j ← 1 to |Leaderboard|
        Peptide ← j-th peptide in Leaderboard
        LinearScores(j) ← LinearScore(Peptide, Spectrum, Alphabet, AminoAcidMass)
    sort Leaderboard according to the decreasing order of scores in LinearScores
    sort LinearScores in decreasing order
    for j ← N + 1 to |Leaderboard|
        if LinearScores(j) < LinearScores(N)
            remove all peptides starting from the j-th peptide from Leaderboard
            return Leaderboard
    return Leaderboard

Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum.
'''
from ch465cyclopeptideSequencing import digitize_spectrum
from ch4112theoriticalspectrum import LinearSpectrum

file = open('/users/fadygamal/Desktop/solvecode/trim.txt', 'r')
data = file.read()
lines = data.split()
Leaderboard = lines
#print(Leaderboard)

file2 = open('/users/fadygamal/Desktop/solvecode/trimspec.txt', 'r')
data2 = file2.read()
lines2 = data2.split()
spectrum = lines2
spectrum = digitize_spectrum(spectrum)
#print(spectrum)
N = 5

def linear_score(peptide, spectrum):            #a function to score the linear peptides
    pep_spectrum = LinearSpectrum(peptide)      #get the liner spectrum of the peptide
    #print(pep_spectrum)
    s = spectrum.copy()                         #copy the spectrum list to remove while iterating later
    count = 0                                   #start a counter
    for mass in pep_spectrum:                   #take every mass in the linear spectrum
        if mass in s:                               #if it is present in the copied spectrum
            count += 1                                  #add a count to your counter
            s.remove(mass)                              #and remove the mass from the copied spectrum
    return count                                        #output the count


def Trim(Leaderboard, spectrum, N):             #a function to select the top scoring N candidate peptides 
    LinearScoresDict = {}                       #an emoty to dict to store the peptide scores
    for Peptide in Leaderboard:                 #take each peptide in the leaderboard
        score = linear_score(Peptide, spectrum)     #get its score of matching the spectrum
        if score not in LinearScoresDict:           #if the score is not already a key in the scores dict
            LinearScoresDict[score] = [Peptide]         #add it and set it value to be a list containing the peptide
        else:                                       #if the score is  already a key in the scores dict
            LinearScoresDict[score].append(Peptide)     #append the peptide to its value list
    #print(LinearScoresDict)
    LinearScores = list(LinearScoresDict.keys())        #make a list of the linear scores collected in the dict
    LinearScores.sort(reverse=True)     #order the scores list in a decending order
    ordered_Leaderboard = []            #make an empty list to order the pepdtides in the leaderboad according to the linear scores order      
    for score in LinearScores:          #take each score in the scores list
        peps_list = LinearScoresDict[score]     #assign it value (list of peptide/s) to a variable
        for pep in peps_list:                   #take each peptide in the value list
            ordered_Leaderboard.append(pep)     #and add it to the empy ordering list 
    #print(LinearScores)
    #print(ordered_Leaderboard)
    LongLinearScores = []               #make an empty list to expand the linear scores for to match the number of the candidate peptides
    for key, value in LinearScoresDict.items():     #take every key and value in the scores dict
        for val in value:                               #and the for peptide in the value list
            LongLinearScores.append(key)                    #add the key (score) to the exanded scores list
    LongLinearScores.sort(reverse=True)             #finally sort the expanded list in a decending order
    #print(LongLinearScores)
    for a in range(N-1, len(Leaderboard)):          #take each peptide in the leaderboars list starting from the Nth position
        if LongLinearScores[a] < LongLinearScores[N-1]:     #if the peptide's score is less the Nth peptide score
            ordered_Leaderboard = ordered_Leaderboard[:a]       #remove all that comes after our peptide from the leaderboard
            return ordered_Leaderboard                          #output the final trimmed leaderboard
    return ordered_Leaderboard                      
                
   
#trimmed = Trim(Leaderboard, spectrum, N)
#for t in trimmed:
    #print(t)