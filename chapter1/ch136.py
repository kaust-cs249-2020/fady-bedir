file = open('/users/fadygamal/Vibrio_cholerae.txt', 'r')
text = file.read()
lines = text.split('\n')

genome = lines[0]
pattern = 'CTTGATCAT'


k = len(pattern)
n = len(genome)

def pattern_find(genome, pattern):

    for i in range(n - k + 1):
        if genome[i : i + k] == pattern: 
            print(i, end=" ")

pattern_find(genome, pattern)



