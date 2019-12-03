#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def fitting_alignment(v,w):
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    j = len(w)
    i = max(enumerate([S[row][j] for row in xrange(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    max_score = str(S[i][j])
    v_aligned, w_aligned = v[:i], w[:j]
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    while i*j != 0:
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
    return max_score, v_aligned, w_aligned

def main():

    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.

    with open('Data/fitting_alignment.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]
    alignment = fitting_alignment(word1, word2)
    print '\n'.join(alignment)

    with open('Data/Answer/fitting_alignment.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

if __name__ == '__main__':

    main()
