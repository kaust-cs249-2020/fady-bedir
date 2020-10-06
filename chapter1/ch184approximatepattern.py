#find approximate patterns locations

file = open('/users/fadygamal/data-ch-1-8-step4.txt', 'r')
txt = file.read()
lines = txt.split('\n')


pattern = lines[0]
text = lines[1]
d = int(lines[2])    #acceptable mismatches

k = len(pattern)
n = len(text)

pos = []
def approx_patt(pattern, text, d):
    for i in range(n - k + 1):
        patt = text[i : i + k]
        count = 0
        for j in range(k):
            if patt[j] != pattern[j]:
                count += 1
        if count <= d:
            pos.append(i)
    return pos

pos_str = approx_patt(pattern, text, d)
print(' '.join(map(str, pos_str)))



    
        


