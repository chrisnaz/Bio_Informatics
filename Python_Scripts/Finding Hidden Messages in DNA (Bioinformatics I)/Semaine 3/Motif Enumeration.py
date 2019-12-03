#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from MisMatchList import kmer_mismatches

def motif_enumeration (k, d, dna_list) :
    motif_sets = [{kmer for i in xrange (len(dna)-k+1) for kmer in kmer_mismatches(dna[i:i+k], d)} for dna in dna_list]
    return sorted(list(reduce(lambda a, b : a & b, motif_sets)))


def main() :
    with open('Motif enumaration.txt') as input_data :
        k, d = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data.readlines()]

    motifs = motif_enumeration(k, d, dna_list)

    print ' '.join(motifs)

    with open('data.txt','w') as output_data :
        output_data.write(' '.join(motifs))

if __name__ == '__main__' :
    main()
