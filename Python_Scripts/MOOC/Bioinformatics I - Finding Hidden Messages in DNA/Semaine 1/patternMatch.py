#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def patternMatch(t,p) :
    pos = []
    i = 0
    for i in range(len(t)) :
        if t[i:i+len(p)] == p :
            pos.append(str(i))
    return " ".join(pos)
