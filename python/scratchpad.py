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
