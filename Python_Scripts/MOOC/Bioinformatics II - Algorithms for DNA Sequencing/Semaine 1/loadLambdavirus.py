#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def loadLambdaVirus(filename) :
    f = open(filename)
    DNA = ''
    for line in f :
        if line[0] != '>' :
            DNA += line.rstrip()
        else :
            h = line.split()
            name = h[0][1:]
    return name, DNA
    
#lambdavirusname, lambdavirusdna = loadLambdaVirus('lambda_virus.fa')