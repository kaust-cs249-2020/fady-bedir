text = "ACTGACTCCCACCCC"
pattern = "ACT"
textlen = len(text)
k = 3 #pattern length

count = 0
counts = []
frequent_pattern = []

for i in range(0, textlen): 
    if pattern == text[i : k + i]: 
        count += 1
        counts.append(count)
        max_count = max(counts)
        if count == max_count:
            frequent_pattern.append(text[i: k + i])
            frequent = list(dict.fromkeys(frequent_pattern))

print(frequent)
        