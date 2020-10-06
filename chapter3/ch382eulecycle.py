from time import time
t1 = time()

file = open('/users/fadygamal/Desktop/solvecode/test.txt', 'r')
data = file.read()
lines = data.split('\n')

def adjacentlist_to_graph(lines):
    nodeslist = []
    for line in lines:
        x = line.index(' ')
        line = [line[:x], line[x+4:]]
        endline = []
        for string in line:
            l = string.split(',')
            endline.append(l)
        nodeslist.append(endline)
    #print(nodeslist)
    bignodes = {}
    for edge in nodeslist:
        for i in range(len(edge[1])):
            if edge[0][0] not in bignodes:
                bignodes[edge[0][0]] = [edge[1][i]]
            else:
                bignodes[edge[0][0]].append(edge[1][i])
    return bignodes

#graph = adjacentlist_to_graph(lines)

def recycle(cycle, newstart):
    #takes a made cycle that's not eulerian and reorders it to continue making a eulerian cycle
    beforenewstart = []  #to store all nodes already used
    cycle = cycle[1:]       #the cycle minus the first node that we tried but didn't a eulerian cycle
    for i in range(len(cycle)):     #check every remaining node
        end = cycle[i]          
        if end == newstart:             #if it's still in the graph dict
            beforenewstart.append(newstart)     #add it to the end of the list 
            return(cycle[i:]+beforenewstart)    #and give a reordered cycle startin with it
        else:                           #if it has been removed from the graph dict i.e. used
            beforenewstart.append(cycle[i])   #add the node to the list of the used nodes and continue the loop
                                            #until the node that is still in the graph dict is the first in the cycle
def euleCycle(graph):
    start = next(iter(graph)) #take the first node in the graph
    node = start
    cycle = [start]         #start building the cycle
    while bool(graph):              #while the graph still unused nodes
        if node not in graph:           #we've got a cycle that's not eulerian
            for end in cycle:           #check every node in cycle 
                if end in graph:        #if it's still in the graph
                    start = end         #reorder the cycle to make it start with it
                    cycle = recycle(cycle, start)
                    node = start
        possibleends = graph[node]      #get the next possible nodes from the graph dict
        if len(possibleends) == 1:
            newstart = possibleends[0]      #if there's only one, make the new start for the next loop
            del graph[node]                 #then delete the whole key, value from the graph
        else:                               #if more than on possible node
            newstart = possibleends[0]         #take the first one and make it the new start for the next loop
            graph[node].remove(possibleends[0]) #then remove its value from the key in graph dict
        cycle.append(newstart)      #finally, add the new start the cycle you're building
        node = newstart             #then set the new start as the node we're at for the next cycle 
    return cycle        #when the graph dict is finally empty, give us the eulerian cycle 

#eulecycle = euleCycle(graph)
#print(eulecycle)

'''def outputeule(eulecycle):
    output = ''
    for i in range(len(eulecycle)-1):
        output += eulecycle[i]+"->"
    output += eulecycle[0]
    return output
    
output = outputeule(eulecycle)
print(output)'''

'''file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(output)
file.close()'''

#t2 = time()
#print("finish after " + str(t2-t1))
