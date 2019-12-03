#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from random import randint
from Greedy_motif_search import score, profile_most_probable_kmer
from Greedy_motif_with_pseudo import profile_with_pseudocounts
# Import defs to avoid duplication.
def gibbs_sampler(dna,k,t,N):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	for i in xrange(N):
		r = randint(0,t-1)
		current_profile = profile_with_pseudocounts([motif for index, motif in enumerate(motifs) if index!=r])
		# print 'a: ', motifs
		motifs = [profile_most_probable_kmer(dna[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
		# print 'b: ', motifs
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	return best_score

if __name__ == '__main__':

	with open('GibbsSampler.txt') as input_data:
		k,t,N = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]

	# Repeat the radomized motif search 20 times.
	for repeat in xrange(20):
		current_motifs = gibbs_sampler(dna_list,k,t,N)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs

	# The collection of strings Best Motifs is printed.
	print '\n'.join(best_motifs[1])
