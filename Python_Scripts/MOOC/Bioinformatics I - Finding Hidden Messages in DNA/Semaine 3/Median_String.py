#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from itertools import product
from HammingDistance import hammingDistance

def median_string (k, dna_list) :
    best = k * len(dna_list) + 1
    for p in product('ACGT', repeat = k) :
        current_score = sum([motif_score(''.join(p), dna) for dna in dna_list])
        if current_score < best :
            best = current_score
            best_p = ''.join(p)
    return best_p

def motif_score(p, modif) :
    return min([hammingDistance(modif[i:i+len(p)], p) for i in range(len(modif)-len(p)+1)])
    
def main() :
    with open('Median_string.txt') as input_data :
        k = int(input_data.readline())
        dna_list = [line.strip() for line in input_data.readlines()]
    best_pattern = median_string(k,dna_list)
    print best_pattern
    
    with open ('pou.txt','w') as output_data :
        output_data.write(best_pattern)
        
if __name__== '__main__' :
    main()
    
