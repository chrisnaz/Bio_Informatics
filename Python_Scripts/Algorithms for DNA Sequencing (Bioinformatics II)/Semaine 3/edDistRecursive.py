#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def edDistRec (a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a == 'Shake' and b == 'shake':
        n += 1
    de = 1
    if a[-1] != b[-1] else 0
    return min (edDistRec (a[:-1], b[:-1]) + de, edDistRec(a[:-1], b) +1, edDistRec (a, b[:-1]) +1)
