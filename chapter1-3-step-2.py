#we have a string and we need to its reverse complement

file = open('/users/fadygamal/dataset.txt', 'r')
text = file.read()
lines = text.split('\n')
string = lines[0]

#print(string) #test if we get the correct input

def rev_string(string):

    def compl_string(string):   #first function to  generate complementary string
        compl_string = ""        
        for i in string:
            if i == "A":                        #used if statment to concatenate nucleotides into empty string
                compl_string += "T"         
            elif i == "T":
                compl_string += "A"
            elif i == "C":
                compl_string += "G"
            else:
                compl_string += "C"
        return compl_string                     #the complementary string now neeed to be reversed

    complement_string = compl_string(string)    #assign the output of the function to a variable  
    reverse_string = complement_string[::-1]    #used slicing with -1 to reverse the order into a new variable
    return reverse_string

print(rev_string(string))






