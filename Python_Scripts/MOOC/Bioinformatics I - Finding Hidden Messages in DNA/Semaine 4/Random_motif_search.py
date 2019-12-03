#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

#This code take some minute to run

from random import randint
from Greedy_motif_search import score, profile_most_probable_kmer
from Greedy_motif_with_pseudo import profile_with_pseudocounts
# Import defs from courseraI355 and courseraI369 to avoid code duplication.
def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def randomized_motif_search(dna,k,t):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	while True:
		current_profile = profile_with_pseudocounts(motifs)
		motifs = motifs_from_profile(current_profile, dna_list, k)
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]
		else:
			return best_score

if __name__ == '__main__' :

	with open('Random_motif_search.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]

	# Repeat the radomized motif search 1000 times.
	for repeat in xrange(1000):
		current_motifs = randomized_motif_search(dna_list,k,t)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs

	# Output collection of best motifs resulting from running code.
	print '\n'.join(best_motifs[1])
