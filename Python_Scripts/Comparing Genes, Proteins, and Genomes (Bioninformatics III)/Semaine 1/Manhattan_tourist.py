#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def manhattan_tourist(n, m, down, right) :
    s = [[0]*(m+1) for i in xrange(n+1)]

    for i in xrange(1, n+1) :
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in xrange(1, m+1) :
        s[0][j] = s[0][j-1] + right[0][j-1]

    for i in xrange(1, n+1) :
        for j in xrange(1, m+1) :
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
    return s[n][m]

def main() :
    with open('Data/Manhattan_tourist.txt') as input_data :
        n, m = map(int, input_data.readline().strip().split())
        down, right = [[map(int, row.split()) for row in matrix.split('\n')] for matrix in input_data.read().strip().split('\n-\n')]

    max_dist = str(manhattan_tourist(n, m, down, right))
    print max_dist

    with open('Data/Answer/Manhattan_tourist.txt','w') as output_data :
        output_data.write(max_dist)

if __name__ == '__main__' :
    main()
