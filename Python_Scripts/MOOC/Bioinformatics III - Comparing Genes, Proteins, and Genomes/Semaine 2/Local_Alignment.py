#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from scripts import PAM250

def local_alignment(v, w, scoring_matrix, sigma):
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    max_score, max_i, max_j = -1, 0, 0

    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], 0]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

            if S[i][j] > max_score:
                max_score, max_i, max_j = S[i][j], i, j

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    i,j = max_i, max_j
    v_aligned, w_aligned = v[:i], w[:j]

    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)

        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)

        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]
    return str(max_score), v_aligned, w_aligned

def main():
    with open('Data/local_alignment.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]
    alignment = local_alignment(word1, word2, PAM250(), 5)
    print '\n'.join(alignment)

    with open('Data/Answer/local_alignment.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

if __name__ == '__main__':
    main()
