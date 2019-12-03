#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def freq_words_with_mn_and_rev_comp(seq, k, d) :
    kmer_freq = defaultdict(int)

    for i in xrange(len(seq)-k+1):

        kmer_freq[seq[i:i+k]] += 1

        kmer_freq[rev_comp(seq[i:i+k])] += 1



    # Get all of the mismatches for each unique k-mer in the sequence, appearing freq times.

    mismatch_count = defaultdict(int)

    for kmer, freq in kmer_freq.iteritems():

        for mismatch in kmer_mismatches(kmer, d):

            mismatch_count[mismatch] += freq



    # Computing the maximum value is somewhat time consuming to repeat, so only do it once!

    max_count = max(mismatch_count.values())

    return sorted([kmer for kmer, count in mismatch_count.iteritems() if count == max_count])
