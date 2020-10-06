file = open("/users/fadygamal/dataset_2.txt", "r")
text = file.read()
lines = text.split('\n')
pattern = lines[1]
k = len(pattern)

freq_map = {}
frequent_patterns = []

def better_freq_words(text, k):
    n = len(text)
    for i in range(0, n - k):
        pattern = text[i : i + k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
  
    maxMap = max(freq_map.values())
    for pattern in freq_map: 
        if freq_map[pattern] == maxMap: 
            frequent_patterns.append(pattern)
    
    print(frequent_patterns)
    



better_freq_words(text, k)