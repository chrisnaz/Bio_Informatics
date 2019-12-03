#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from Greedy_motif_search import profile_most_probable_kmer
from Greedy_motif_search import score

def profile_with_pseudocounts(motifs) :
    colu = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) /float(len(col)+4) for nuc in 'ACGT'] for col in colu]

def greedy_motif_search_pseudocounts(dna, k, t) :
    best_score = t*k

    for i in xrange(len(dna[0])-k+1) :
        motifs = [dna[0][i:i+k]]

        for j in xrange(1, t) :
            current_profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, current_profile))

        current_score = score(motifs)
        if current_score < best_score :
            best_score = current_score
            best_motifs = motifs

    return best_motifs

def main() :
    with open ('greedy_motif_search_pseudocounts.txt') as input_data :
        k, t = map(int, input_data.readline().split())
        dna = [line.strip() for line in input_data]
    best_motifs = greedy_motif_search_pseudocounts(dna, k, t)

    print '\n'.join(best_motifs)
    with open('greedy_motif_search_pseudocounts_an.txt', 'w') as output_data :
        output_data.write('\n'.join(best_motifs))

if __name__ == '__main__' :
    main()
