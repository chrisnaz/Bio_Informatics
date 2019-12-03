#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def profile_most_profile_kmer (dna, k, profile) :
    nuc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    max_prob = -1

    for i in xrange(len(dna)-k+1) :
        cur_prob = 1
        for j, nucleotide in enumerate(dna[i:i+k]) :
            cur_prob += profile[j][nuc[nucleotide]]

        if cur_prob > max_prob :
            max_prob = cur_prob
            most_probable = dna[i:i+k]

    return most_probable

def main() :
    with open('exmple.txt') as input_data :
        dna = input_data.readline().strip()
        k = int(input_data.readline())
        profile = [map(float,line.strip().split()) for line in input_data.readlines()]

    most_probable = profile_most_profile_kmer(dna,k,profile)
    print most_probable
    with open('name','w') as output_data :
        output_data.write(most_probable)

if __name__ == '__main__' :
    main()
