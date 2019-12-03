#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def hammingDistance(x, y):
    n = 0
    for i in xrange(0, len(x)):
        if x[i] != y[i]:
            n += 1
    return n
