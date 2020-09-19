import math
nucleotides = ['A', 'C', 'G', 'T']
motifs = [
    ['TCGGGGGTTTTT'],
    ['CCGGTGACTTAC'],
    ['ACGGGGATTTTC'],
    ['TTGGGGACTTTT'],
    ['AAGGGGACTTCC'],
    ['TTGGGGACTTCC'],
    ['TCGGGGATTCAT'],
    ['TCGGGGATTCCT'],
    ['TAGGGGAACTAC'],
    ['TCGGGTATAACC']
]

k =12

def motif_to_matrix(motifs):
    motifmatrix = []
    for item in motifs:
        for i in range(len(item)):
            motifdivided = []
            motif = item[i]
            for j in motif:
                motifdivided.append(j)
            motifmatrix.append(motifdivided)
    return motifmatrix

def score(motifs, k):
    motifsmatrix = motif_to_matrix(motifs)
    empty = []
    for f in range(len(motifsmatrix[0])):
        emptyrow = []
        for g in range(len(motifsmatrix)):
            emptyrow.append('')
        empty.append(emptyrow)
    
    for item in motifsmatrix:
        if item == []:
            for s in range(len(motifsmatrix[0])):
                item.append('')

    score = 0
    scorematrix = []
    columns = empty

    for i in range(len(motifsmatrix)):
        for j in range(len(motifsmatrix[0])):
            columns[j][i] = motifsmatrix[i][j]
        
    for column in columns:
        freq_map = {}
        for i in range(len(column)):
            nucleotide = column[i]
            if nucleotide == "":
                continue
            elif nucleotide not in freq_map:
                freq_map[nucleotide] = 1
            else:
                 freq_map[nucleotide] += 1
        
        def max_value(freq_map): 
            max_v = 0
            for value in freq_map.values():
                if value > max_v:
                    max_v = value
            return max_v
        
        unpopular = len(column) - max_value(freq_map)
        score += unpopular
        scorematrix.append(freq_map)
    
    for dic in scorematrix:
        for n in nucleotides:
            if n not in dic:
                dic[n] = 0

    ord_scorematrix = []
    for dic1 in scorematrix:
        dic2 = {}
        for key in sorted(dic1.keys()):
            dic2[key] = dic1[key]
        ord_scorematrix.append(dic2)
    
    scorecolumns = []
    for d in ord_scorematrix:
        scorecolumn = []
        for key, value in d.items():
            scorecolumn.append(value)
        scorecolumns.append(scorecolumn)
    
    emptymat = []
    for a in range(len(nucleotides)):
        emptyrow = []
        for b in range(k):
            emptyrow.append(0)
        emptymat.append(emptyrow)
    
    for x in range(len(scorecolumns)):
        for y in range(len(scorecolumns[0])):
            emptymat[y][x] = scorecolumns[x][y]
    
    return score, emptymat

def prof_matrix(motifs, k):
    scored = score(motifs, k)
    count_matrix = scored[1]
    
    tots = []
    for i in range(len(count_matrix[0])):
        col_total = 0
        for j in range(len(count_matrix)):
            col_total += count_matrix[j][i]
        tots.append(col_total)
    
    profile = []
    denom = tots[0]
    for x in range(len(count_matrix)):
        row = count_matrix[x]
        pr = []
        for y in range(len(row)):
            num = row[y] / denom
            pr.append(num)
        profile.append(pr)
    
    return profile
    
def entropy(profile_matrix):
    entropy = 0
    for i in range(len(profile_matrix[0])):
        entropy1 = 0
        for j in range(len(profile_matrix)):
            value = profile_matrix[j][i]
            if value == 0:
                entropy1 += 0
            else:
                log = math.log(value, 2)
                ent = value * log
                entropy1 -= ent
        entropy += entropy1

    return entropy

