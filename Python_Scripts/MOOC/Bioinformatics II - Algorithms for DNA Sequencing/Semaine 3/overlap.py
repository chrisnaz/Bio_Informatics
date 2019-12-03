#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from itertools import permutations

def overlap(a, b, min_lenght=3) :
    start = 0
    while True :
        start = a.find(b[:min_lenght], start)
        if start == -1 :
            return 0
        if b.startswith(a[start:]) :
            return len(a) - start
        start += 1
