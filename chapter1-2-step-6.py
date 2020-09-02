#we have a string of text and a pattern, and we need to figure out how many times the pattern was repeated in the text

file = open("/users/fadygamal/dataset_2.txt", "r") #open txt file in reading mode
text = file.read() #store content in variable: text
lines = text.split("\n") #split the lines of text into items in a list called lines
text = lines[0] #reassign the variable text to the first item of the list lines
pattern = lines[1] #reassign the variable pattern to the second item of the list lines

textlen = len(text) #assign the length of the text string to the varibable textlen (in material: |text| - k)
patternlen = len(pattern) #assign the length of the pattern string to the varibable patternlen (k in k-mer)


def pattern_count(text, pattern): #define the function for counting the pattern within text
    count = 0 
    for i in range(0, textlen - patternlen + 1):        # for loop add 1 count each time the sliced string
        if text[i : patternlen + i] == pattern:         # matches the pattern
            count += 1                         
            
    return count

print('pattern was repeated ' + str(pattern_count(text,pattern)) + ' times')





