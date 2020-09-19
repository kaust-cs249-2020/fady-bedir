from hammingdistance import hum_dist
from neighborhood import neighbors
file = open('/users/fadygamal/medianstr.txt', 'r')
content = file.read()
lines = content.split('\n')

#we want to determine the minimum distance between a pattern and a collection of strings 
'''
#inputs
texts = lines #collection of DNA strings
pattern = 'CTTCA' #the pattern whose distance to the DNA strings in text we want to determine'''



def dist_pattern_strings(pattern, texts):
    distance = 0
    k = len(pattern)
    for text in texts:
        ham_dist = float('inf')
        for i in range(len(text) - k + 1):
            test_pat = text[i : i+k]
            if hum_dist(test_pat, pattern) < ham_dist:
                ham_dist = hum_dist(test_pat, pattern)
        distance += ham_dist
    return distance

'''distance = dist_pattern_strings(pattern, texts)
print(distance)'''

#function to find all possible patterns of length k in a text

def allstrings(text, k):
    all = []
    for i in range(len(text) - k + 1):
       pattern = text[i : i + k]
       all.append(pattern)
       neighborhood = neighbors(pattern, k)
       for neighbor in neighborhood:
           all.append(neighbor)
    return all

texts = lines[1:]
k = int(lines[0])

#print(texts)
#print(k)

#function to find the median string that acheives the minimum sum of distances between a pattern of length k and 
#all strings in the collection texts 

def medianstring(texts, k):
    distance = float('inf')
    median = []
    for text in texts:
        patterns = allstrings(text, k)
        for pattern in patterns:
            if dist_pattern_strings(pattern, texts) < distance:
                distance = dist_pattern_strings(pattern, texts)
                median.append(pattern)
    return median 

print(medianstring(texts, k))