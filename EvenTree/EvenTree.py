"""
You are given a tree (a simple connected graph with no cycles).You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest contains even number of vertices

Your task is to calculate the number of removed edges in such a forest.

Input:
The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges. 2 <= N <= 100. 
Next M lines contains two integers ui and vi which specifies an edge of the tree. (1-based index)

Output:
Print a single integer which is the answer

Sample Input 

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
 
Sample Output :
2
"""

import sys

leafs = []
def findLeafNodes() :
    x = len(parentToChildren) - 1
    while x >= 0 :
        if len(parentToChildren[x]) == 0:
            leafs.append(x)
        x-=1

def makeForests() :
    findLeafNodes()
    for n in leafs:
        p = traverseAndSever(n)
    

def traverseAndSever(n) :
    x = n
    while nodeToParent[x] != -1 :
        if (countChildren(nodeToParent[x]) + 1) % 2 == 0 :
            parent = nodeToParent[nodeToParent[x]] 
            sever(parent, nodeToParent[x])
        x = nodeToParent[x]

def sever(parent, child) :      
    nodeToParent[child] = -1
    if child in parentToChildren[parent]:
        parentToChildren[parent].remove(child)
        if len(parentToChildren[parent]) == 0 :
            leafs.append(parent)

def countChildren(p) :
    c = len(parentToChildren[p])
    for n in parentToChildren[p] :
        c += countChildren(n)
    return c

def countForests() :
    y = 1
    count = 0 
    while y < len(nodeToParent) :
        if(nodeToParent[y] == -1):
            count +=1 
        y+=1
    return count

f = sys.stdin
numVertices = int(f.readline().split()[0])
nodeToParent = [-1 for x in range(numVertices)]
parentToChildren = [[] for x in range(numVertices)] 
for line in f:
    child = int(line.split()[0]) - 1
    parent = int(line.split()[1]) - 1
    nodeToParent[child] = parent 
    parentToChildren[parent].append(child) 


makeForests()
print countForests()
