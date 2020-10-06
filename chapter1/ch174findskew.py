#the point where the difference between G and C stops decreasing and starts increasing is believed to be the ori

#skew = G - C

file = open('/users/fadygamal/data-ch1-7-step-6.txt', 'r')
text = file.read()
lines = text.split('\n')

genome = lines[0]



def find_skew(genome):
    n = len(genome)
    skews = []
    for i in range (n + 1):
        gen = genome[0 : i]
        skew = gen.count("G") - gen.count("C")
        skews.append(skew)
    return skews


skews_list = find_skew(genome)
print(' '.join(map(str, skews_list)))




