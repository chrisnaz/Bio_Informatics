#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def clumFinding(ge,k,l,t) :
    f = []
    c = []
    for i in range(4**k - 1 + 1) :
        c[i] = 0
    for i in range(len(ge) - l + 1) :
        t = ge[i:i+l]
        fa = computingFreqs(t,k)
        for index in range(4**k-1+1) :
            if fa[index] >= t :
                c[index] = 1
    for i in range(4**k) :
        if c[i] == 1 :
            pa = numberToPattern(i,k)
            f.append(pa)
    return f

def computingFreqs(Text, k):
    textList = list(Text)
    frequencyArray = []
    for i in range(4**k-1+1):
        frequencyArray.insert(i, 0)
    for i in range(len(textList)-k+1):
        pattern = textList[i:i+k]
        j = patternToNumber(pattern)
        x = frequencyArray[j] + 1
        frequencyArray[j] += 1
    return frequencyArray

def numberToSymbol(number):
    symbol = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}
    return symbol
    """if number == 0:
        symbol = "A"
    elif number == 1:
        symbol = "C"
    elif number == 2:
        symbol = "G"
    elif number == 3:
        symbol = "T"
    return symbol"""

def numberToPattern(index,k):
    if k == 1:
        return numberToSymbol(index)
    prefixIndex = index/4
    r = index % 4
    symbol = numberToSymbol(r)
    prefixPattern = numberToPattern(prefixIndex,k-1)
    return prefixPattern + symbol
