#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def global_alignment(v, w, scoring_matrix, sigma):
    S = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
    backtrack = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]

    for i in xrange(1, len(v)+1):
        S[i][0] = -i*sigma

    for j in xrange(1, len(w)+1):
        S[0][j] = -j*sigma

    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    v_aligned, w_aligned = v, w
    i, j = len(v), len(w)
    max_score = str(S[i][j])

    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    for repeat in xrange(i):
        w_aligned = insert_indel(w_aligned, 0)
    for repeat in xrange(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned

if __name__ == '__main__':
    from scripts import BLOSUM62

    # Read the input data.
    with open('Data/global_alignment.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the alignment.
    alignment = global_alignment(word1, word2, BLOSUM62(), 5)

    # Output result.
    print '\n'.join(alignment)
    with open('Data/Answer/global_alignment.txt','w') as output_data :
        output_data.write('\n'.join(alignment))
