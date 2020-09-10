# we have a string of text and the length of the pattern, and we figure out the frequent patterns or k-mers

file = open('/users/fadygamal/dataset_3.txt', 'r')
text = file.read()
lines = text.split('\n')

text = lines[0]
n = len(text)
k = int(lines[1])

freq_map = {}
freq_pattern = []

def better_freq(text, k):
    for i in range(0, n - k + 1):               #for loop that creates a key in the dict and assigns a value of 1 
        pattern = text[i : i + k]       #if the key is already they, loop adds 1 to its value
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else: 
            freq_map[pattern] += 1

    
    def maxMap(freq_map):                   # a function to determine the max value in a dictionnary
        max_value = 0 
        for key, value in freq_map.items():
            if value > max_value:
                max_value = value
        return max_value
    
    for pattern in freq_map:            #for loop that checks the value every key in the dict,
        if freq_map[pattern] == maxMap: #if it matches the max value, the key is added to a list 
            freq_pattern.append(pattern)
    
    print("the pattern is "+ str(freq_pattern))
    print("it was repeated " + str(maxMap(freq_map)) + " times")

better_freq(text, k)
