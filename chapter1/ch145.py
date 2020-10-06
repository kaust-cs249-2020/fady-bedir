#finding the clumps of length l where a k-mer is repeated t times

file = open('/users/fadygamal/E_coli.txt', 'r')
text = file.read()
lines = text.split('\n')


gen = lines[0]
k = 9
l = 500
t = 3
n = len(gen)

print(n)

patterns = []

def find_c(gen,k,l,t):
    for i in range(n-l+1):
        win = gen[i:i+l]
        freq = {}
        for j in range(l-k+1):
            pat = win[j:j+k]
            if pat not in freq:
                freq[pat] = 1
            else:
                freq[pat] += 1
            for pat in freq:
                if freq[pat] >= t:
                    patterns.append(pat)
   
    pat_f_dup = list(dict.fromkeys(patterns))
    return pat_f_dup

print(find_c(gen,k,l,t))


