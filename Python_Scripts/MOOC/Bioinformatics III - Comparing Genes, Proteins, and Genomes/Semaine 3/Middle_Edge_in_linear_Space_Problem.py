#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from scripts import BLOSUM62

def middle_column_score(v, w, scoring_matrix, sigma):

    '''Returns the score of the middle column for the alignment of v and w.'''

    # Initialize the score columns.
    S = [[i*j*sigma for j in xrange(-1, 1)] for i in xrange(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0]*(len(v)+1)

    for j in xrange(1, len(w)/2+1):
        for i in xrange(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)/2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack

def middle_edge(v, w, scoring_matrix, sigma):
    source_to_middle = middle_column_score(v, w, scoring_matrix, sigma)[0]
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))
    scores = map(sum, zip(source_to_middle, middle_to_sink))
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node

def main():
    with open('Data/Middle_Edge_in_linear_Space_Problem.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]
    middle = middle_edge(word1, word2, BLOSUM62(), 5)

    print ' '.join(map(str, middle))
    with open('Data/Answer/Middle_Edge_in_linear_Space_Problem.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, middle)))

if __name__ == '__main__':
    main()
