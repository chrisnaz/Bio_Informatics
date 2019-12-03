#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def longest_common_sbsequence(v, w):
    S = [[0]*(len(w)+1) for _ in xrange(len(v)+1)]
    for i in xrange(len(v)):
        for j in xrange(len(w)):
            if v[i] == w[j]:
                S[i+1][j+1] = S[i][j]+1
            else:
                S[i+1][j+1] = max(S[i+1][j],S[i][j+1])

    longest_sseq = ''
    i,j = len(v), len(w)
    while i*j != 0:
        if S[i][j] == S[i-1][j]:
            i -= 1
        elif S[i][j] == S[i][j-1]:
            j -= 1
        else:
            longest_sseq = v[i-1] + longest_sseq
            i -= 1
            j -= 1
    return longest_sseq

def main():
    with open('Data/Longest_Common_Subsequence.txt') as input_data:
        dna1, dna2 = [line.strip() for line in input_data.readlines()]
    longest_subseq = longest_common_sbsequence(dna1, dna2)
    print longest_subseq

    with open('Data/Answer/Longest_Common_Subsequence.txt', 'w') as output_data:
        output_data.write(longest_subseq)

if __name__ == '__main__':

    main()
