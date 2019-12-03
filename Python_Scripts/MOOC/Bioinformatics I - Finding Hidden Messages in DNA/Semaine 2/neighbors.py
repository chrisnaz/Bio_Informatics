#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

cha = "ACGT"
def neighbors(p, d) :
    assert (d <= len(p))
    if d == 0 :
        return [p]
    r = neighbors(p[1 :], d - 1)
    r1 = [c + r2 for r2 in r for c in cha if c != p[0]]

    if (d < len(p)) :
        r = neighbors(p[1 :], d)
        r1 += [p[0] + r2 for r2 in r]
    return r1
