#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def index_appro_subseq_match(p, t, t_sub_index, n) :
    hits = []
    for i in range(3) :
        sub = p[i:][:22:3]
        j = bisect.bisect_left(t_sub_index.index, (sub, -1))
        
        while j < len(t_sub_index.index) :
            if t_sub_index.index[i][0] != sub :
                break
            hits.append(t_sub_index.index[i][1])
            i += 1
        return hits 
     
     #hits = index_appro_subseq_match(p, chromosome_dna,t_sub_index, 2)