#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def naiv_2(p,t) :
    appar = []
    for i in range(len(t) - len(p) +1) :
        mismatch = 0
        for j in range (len(p)) :
            if t[i+j] != p[j] :
                mismatch += 1
                if mismatch == 3 :
                    break
        if mismatch <= 2 :
            appar.append(i)
    return appar