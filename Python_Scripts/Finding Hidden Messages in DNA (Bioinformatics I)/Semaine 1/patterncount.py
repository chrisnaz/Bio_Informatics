#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def PatternCount(t, p) :
    count = 0
    i = 0
    for i in range (len(t) - len(p)) :
        if t[i: len(p) +i] == p :
            count += 1
    return count

