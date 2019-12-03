#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

"""def read(filename):
    with open(filename, 'r') as f :
        f.readline()
        text = f.readline()
        k = f.readline()
        return text.strip(), int(k.strip())
        
    if __name__== "__main__" :
        test, k = read('dataset.txt')
        result = frequentWords (t,k)
        print result"""
        
def frequentWords(t,k) :
    frepat = []
    tlist = list(t)
    count = []
    
    for i in range(len(tlist)-k+1) :
        p = t[i:i+k]
        count.insert(i,PatternCount(t,p))
        #we can print pattern, count
    maxcount = max(count)
    
    for i in range(len(tlist)-k+1) :
        if count[i] == maxcount :
            frepat.append(t[i:i+k])
    return frepat
    
def PatternCount(t, p) :
    count = 0
    i = 0
    for i in range (len(t) - len(p)) :
        if t[i: len(p) +i] == p :
            count += 1
    return count

