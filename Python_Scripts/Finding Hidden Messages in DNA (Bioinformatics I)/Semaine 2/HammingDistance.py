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
def op(filename):
    x = []
    y = []
    filename = raw_input('Enter the file name : ')
    try :
        filenames = open(filename)
    except :
        print'This file ',filename, ' cannot be opened'
        exit()
    x, y = [line.strip() for line in filenames.readlines()]
