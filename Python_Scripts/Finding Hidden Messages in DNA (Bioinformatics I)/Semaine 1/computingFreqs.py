#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

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

def symbolToNumber(symbol):
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number

def patternToNumber(Pattern):
    #pdb.set_trace()
    patternList = list(Pattern)
    if not patternList:
        return 0
    symbol = patternList[-1]
    prefix = patternList[:-1]
    #print symbol, prefix
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)


