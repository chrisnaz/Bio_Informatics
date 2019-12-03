#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def loadFasta(filename) :
    f = open(filename)
    name = ''
    dna = ''
    for line in f :
        if line[0] == '>' :
            name = line[1:].rstrip()
        else :
            dna += line.rstrip()
    return name, dna