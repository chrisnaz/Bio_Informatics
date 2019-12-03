#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from HammingDistance import hammingDistance

def score(motifs):
	'''Returns the score of the dna list motifs.'''
	score = 0
	for i in xrange(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		score += min([hammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
	return score

def profile(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof

def profile_most_probable_kmer(dna, k, prof):
	'''Return the profile most probable k-mer in a given dna sequence.'''
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	max_prob = [-1, None]

	for i in xrange(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]

if __name__ == '__main__':

	with open('Greedy_motif.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	best_score = [t*k, None]

	for i in xrange(len(dna_list[0])-k+1):
		motifs = [dna_list[0][i:i+k]]
		current_profile = profile(motifs)

		for j in xrange(1,t):
			motifs.append(profile_most_probable_kmer(dna_list[j],k,current_profile))
			current_profile = profile(motifs)

		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	# Write collection of strings.
	print '\n'.join(best_score[1])
	'''with open('Greedy_motif_answer.txt','w') as output_data :
                output_data.write('\n'.join(best_score)'''
