#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from itertools import permutations
from overlap import overlap

def naive_overlap_map(reads, k) :
    claps = {}
    for a, b in permutations(reads, 2) :
        ol = overlap(a, b, min_lenght=k)
        if ol > 0 :
            claps[(a, b)] = ol
    return claps
    
def readFASTQ (filename) :
    f = open(filename)
    r = []
    while True :
        h = f.readline()
        if len(h) == 0 :
            break
        se = f.readline().rstrip()
        _ = f.readline()
        q = f.readline().rstrip()
        r.append(se)
    return r
    
'''file='ERR255411_1.fot_asm.fastq'
r = readFASTQ(file)
%%time
overlap = naive_overlap_map(reads, 30)
len(overlap)
'''
