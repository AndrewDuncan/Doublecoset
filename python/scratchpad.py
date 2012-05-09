import os
import itertools

inedges = {}
inedgesList = []

def addInEdge(label,v):
    if (label,v) in inedgesList:
        return
    else:
        inedgesList.append((label,v))
    if not label in inedges:
        inedges[label] = [v]
    elif not v in inedges[label]:
        inedges[label].append(v)


def addVertex():
    vertexCount += 1
    v=Vertex(vertexCount)
    vertices.append(v)
    return v

word='abcde'
lastvadded = 0
nextlabel = word[0]
penul = len(word)-1
for c in word[1:penul]:				#for each letter in the word except the first and last:
	print "letter is ", c, "prev letter is ", nextlabel, "lastvadded is ", lastvadded
        nextlabel = c
        lastvadded += 1
        

        
