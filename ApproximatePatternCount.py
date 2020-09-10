#ApproximatePatternCount

from hammingdistance import ham_dist

file = open('/users/fadygamal/data-ch-1-8-step6.txt', 'r')
txt = file.read()
lines = txt.split('\n')

pattern = lines[0]
text = lines[1]
d = int(lines[2])

k = len(pattern)
n = len(text)

def app_patt_count(pattern, text, d):
    count = 0
    for i in range(n - k + 1):
        patt = text[i : i + k]
        ham = ham_dist(pattern, patt)
        if ham <= d:
            count += 1
    return count

print(app_patt_count(pattern, text, d))
