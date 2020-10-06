# find the hamming distance
# the hamming distance is the number of mismatches between 2 strings 
'''
file = open('/users/fadygamal/data-ch-1-8-step3.txt', 'r')
text = file.read()
lines = text.split('\n')


string1 = lines[0]
string2 = lines[1]
'''

def hum_dist(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count




        





