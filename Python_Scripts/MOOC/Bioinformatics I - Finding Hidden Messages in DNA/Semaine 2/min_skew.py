#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def skew (message) :
    c = 0
    g = 0
    min_skew = 0
    s_list = []
    i = 0

    for j in message :
        i += 1
        if j == 'C' :
            c += 1
        if j == 'G' :
            g += 1
        skew = g - c
        if skew < min_skew :
            s_list = [i]
            min_skew = skew
        if skew == min_skew and i not in s_list :
            s_list.append(i)
    print (s_list)

    #with open ('min_skew.txt','r') as in_file :
        #message = in_file.readline()
        #skew(message)

        
