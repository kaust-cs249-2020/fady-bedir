from time import time
t1 = time()

from eulecycle import euleCycle

'''file = open('/users/fadygamal/Desktop/solvecode/eulepath.txt', 'r')
data = file.read()
lines = data.split('\n')'''

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
#print(graph)

def find_unbalanced_nodes(graph):
    start = 0
    end = 0
    keys = list(graph.keys())        #make a list of all nodes
    for values in graph.values():
        for value in values:
            if value not in keys:
                keys.append(value)  #make sure all nodes are on the list
    for key in keys:
        if key not in graph:    #if a node is not a key in the graph dict
            outgoing = 0        #then it has no outgoing edges
        else:
            outgoing = len(graph[key])   #if it's a key then get the number of its outgoing edges
        incoming = 0
        for values in graph.values():
            if key in values:           #if a node is in both keys and values of the graph dict
                incoming += 1           #then add 1 to its incoming edges number
        if outgoing > incoming:         
            start = key                 #if more edges are leaving than entering a node, this is the start of the path
        elif incoming > outgoing:
            end = key                   # if more edges are enterin than leving a node, this is the end of the path
    return start, end

def eulePath(graph):
    start, end = find_unbalanced_nodes(graph)  #get the start and end nodes
    if end not in graph:            #balance the graph to use the cycle function from before
        graph[end] = [start]
    else:
        graph[end].append(start)
    path = euleCycle(graph)        #get a euelerian cycle
    
    for i in range(len(path)):                      #find the end node
        if path[i] == end:                          
            path = path[i+1:] + path[1:i+1]         #and rearrange the path to make the end node at the end of the path
            break                                   #once you find it stop the loop
    return path
'''
eulepath = eulePath(graph)

def outputeulepath(eulepath):
    output = ''
    for i in range(len(eulepath)-1):
        output += eulepath[i]+"->"
    output += eulepath[-1]
    return output
    
output = outputeulepath(eulepath)
#print(output)'''

'''file = open("/users/fadygamal/Desktop/out.txt", "w")
file.write(output)
file.close()

t2 = time()
print("finish after " + str(t2-t1))'''
