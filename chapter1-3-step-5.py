#we have a genome and a pattern, and we're looking for the positions at which the pattern reappears

file = open("/users/fadygamal/dataset.txt", "r")
text = file.read()
lines = text.split('\n')

pattern = lines[0]
genome = lines[1]

k = len(pattern)
n = len(genome)

def pattern_find(pattern, genome): 
    
    for i in range(n - k + 1):                  #for loop where each time the pattern matches the sliced genome string 
        if genome[i : i + k] == pattern:        #the position of the first letter is printed 
            print (i, end=" ")

pattern_find(pattern, genome)
