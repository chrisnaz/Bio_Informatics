#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def find_pattern(p,q,d) :
    count = 0
    for x,  y in zip(p,q) :
        if x != y :
            count = count + 1
        if count >  d :
            return False
    return True

def app_pattern_mat_problem(p, t, d) :
    pos = []
    for i in range(len(t) - len(p)) :
        if find_pattern(p, t[i: i + len(p)], d) :
            pos = pos + [i]
    return pos
#string = "".join(open("dataset_9_4.txt")).split()
#app_pattern_mat_problem(string[0], string[1], int(string[2]))
