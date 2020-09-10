file = open('/users/fadygamal/data-ch1-7-step-6.txt', 'r')
text = file.read()
lines = text.split('\n')

genome = lines[0]
n = len(genome)

#1 find skews 
skews = []
def find_skew(genome):
    for i in range (n + 1):
        win = genome[0 : i]
        skew = win.count("G") - win.count("C")
        skews.append(skew)
    return skews

skews_list = find_skew(genome)
        
#2 find location of min skews

locations = []
def find_loc(genome):
    min_value = min(skews_list)
    for i in range(len(skews_list)):
        if skews_list[i] == min_value:
            locations.append(i)

    return locations

locations_list = find_loc(genome)

locations_str = ' '.join(map(str, locations_list))
print(locations_str)

