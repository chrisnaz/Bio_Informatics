#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def edit_distance(v,w):
    M = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    for i in range(1,len(v)+1):
        M[i][0] = i

    for j in range(1,len(w)+1):
        M[0][j] = j

    for i in xrange(1,len(v)+1):
        for j in xrange(1,len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    return M[len(v)][len(w)]

def main():
    with open('Data/Edit_distance.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    e_dist = edit_distance(word1, word2)
    print str(e_dist)
    with open('Data/Answer/Edit_distance.txt', 'w') as output_data:
        output_data.write(str(e_dist))

if __name__ == '__main__':
    main()
