

file = open("/users/fadygamal/dataset_2.txt", "r")

def pattern_analysis(x): 
   
    text = x.read()                 #opened the file in read mode 
    lines = text.split("\n")        #split lines into a list    
    text = lines[0]                 #assigned items into varibales 
    pattern = lines[1]

    textlen = len(text) # referred to |text|-k
    patternlen = len(pattern) # referred to as k in material

    count = 0
    counts = []
    frequent = []

    for i in range(0, textlen):                       #for loop that adds a count each time the slice matches pattern
        if pattern == text[i : i + patternlen]:       #and then adds adds each count to the list counts    
            count += 1 
            counts.append(count)
            max_count = max(counts)                   #variable assigned to the maximum value in counts
            if count == max_count:                              #when the counts match the maximum value, 
                frequent.append(text[i : i + patternlen])       #the slice will be added the list 
                frequent_pattern = list(dict.fromkeys(frequent))   #removing duplicate by creating a dictionary and
                                                                    #turning it back to a list
                

    print('pattern is ' + str(frequent_pattern[0]))
    print('pattern was repeated ' + str(count) + ' times')


pattern_analysis(file)

