from time import time
t1 = time()
'''
 LeaderboardCyclopeptideSequencing(Spectrum, N)
        Leaderboard ← set containing only the empty peptide
        LeaderPeptide ← empty peptide
        while Leaderboard is non-empty
            Leaderboard ← Expand(Leaderboard)
            for each Peptide in Leaderboard
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                        LeaderPeptide ← Peptide
                else if Mass(Peptide) > ParentMass(Spectrum)
                    remove Peptide from Leaderboard
            Leaderboard ← Trim(Leaderboard, Spectrum, N)
        output LeaderPeptide
'''
from ch465cyclopeptideSequencing import digitize_spectrum
from ch465cyclopeptideSequencing import Expand
from ch465cyclopeptideSequencing import Mass
from ch465cyclopeptideSequencing import peptide_to_masses
from ch4133trimming import Trim
from ch4133trimming import linear_score
from ch473cyclopepscore import cyclopep_score

file = open('/users/fadygamal/Desktop/solvecode/leadersequence.txt', 'r')
data = file.read()
lines = data.split()

N = 1000
spectrum = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'
spectrum = spectrum.split()
spectrum = digitize_spectrum(spectrum)

def LeaderboardCyclopeptideSequencing(Spectrum, N): #a function to obtain a cyclic peptide sequence from an experimental spectrum
    ParentMass = Spectrum[-1]       #set the parent mass as the biggest mass in the spectrum
    leaderPeptide = ''              #start with an empty peptide as the leader
    leaderboard = ['']   #and a leaderboard containing the leader peptide
    #leaders = []
    while len(leaderboard) > 0:             #while the leaderboard is not empty
        leaderboard = Expand(leaderboard)       #expand each candidate peptide
        #print(leaderboard)
        for peptide in leaderboard[:]:          #then take each  candidate peptide    
            if Mass(peptide) == ParentMass:     #if its mass is equal to the biggest mass in the spectrum 
                if linear_score(peptide, Spectrum) > linear_score(leaderPeptide, Spectrum):     #and it's matching spectrum score is bigger than that of the starting leader
                    #leaders = [[peptide, cyclopep_score(peptide, Spectrum)]]
                    leaderPeptide = peptide              #then set this candidate as the new leader
                #elif linear_score(peptide, Spectrum) == linear_score(leaderPeptide, Spectrum):
                    #leaders.append([peptide, cyclopep_score(peptide, Spectrum)])
            elif Mass(peptide) > ParentMass:     #but if its mass is larger to the biggest mass in the spectrum
                leaderboard.remove(peptide)                     #then get rid of this candidate
        leaderboard = Trim(leaderboard, Spectrum, N)    #afterwards, get the highest scoring N leaders
        #print(leaderboard)
        #break
    #leaderPeptideMass = peptide_to_masses(leaderPeptide)    #finally get a list of the masses of the leader peptide
    return leaderPeptide                                

leader = LeaderboardCyclopeptideSequencing(spectrum, N)

#for item in leaders:
    #print (peptide_to_masses(item[0]))

t2 = time()
print(t2 - t1)


