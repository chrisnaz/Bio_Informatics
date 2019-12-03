#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from itertools import imap
from operator import ne

def hammingDistance(x, y):
    if len(x) != len(y) :
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(imap(ne, x, y))