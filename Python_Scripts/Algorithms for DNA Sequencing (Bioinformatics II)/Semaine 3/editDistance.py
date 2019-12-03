#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def loadFasta (filename) :
    f = open (filename)
    name = ''
    dna = ''

    for line in fil :
        if line[0] == '>' :
            name = line[1:].rstrip()
        else :
            dna += line.rstrip()
    return  name, dna

#chromosome_name, chromosome_dna = loadFasta('chr1.GRCh38.excerpt.fasta')

def editDistance (x, y) :
    d = []
    for i in range (len(x) +1) :
        d.append([0]*(len(y)+1)

    for i in range (len(x)+1):
        d[i][0] = i
    for i in range (len(y)+1) : 
        d[0][i] = 0
    for i in range (1, len(x)+1):
        for j in range (1, len(y)+1) :
            dh = d[i][j-1] + 1
            dv = d[i-1][j] + 1
            if x[i-1] == y[j-1] :
                disD = d[i-1][j-1]
            else :
                disD = d[i-1][j-1] +1
            d[i][j] = min(dh, dv, disD)
    distance = d[-1]
    distance.sort()
    return distance[0]
    
