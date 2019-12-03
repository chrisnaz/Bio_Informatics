import collections
import random

def readLambdaVirus (file):
        genome = ''
        with open (file, 'r') as f:
                for line in f :
                        if not line[0] == '>':
                                genome += line.rstrip()
        return genome

def naiv (p,t):
        occ = []
        for i in range (len(t) - len(p) +1) :
                match = True
                for j in range (len(p)) :
                        if t[i+j] != p[j] :
                                match = False
                                break
                if match :
                        occ.append(i)
        return occ

def genReads (genome, numReads, readLen) :
        reads = []
        for _ in range (numReads) :
                start = random.randint(0, len(genome)-readLen) - 1
                reads.append(genome[start : start+readLen])
        return reads
        Number = 0
        for r in reads :
                matches = naive(r, genome)
                if len(matches) > 0 :
                        Number += 1
        print ('%d matches' % (Number))

def naiv_2mm (p, t) :
        occ = []
        for i in range (len(t) - len(p) + 1) :
                mismatch = False
                for j in range (len(p)) :
                        if t[i+j] != p[j] :
                                mismatch = True
                                break
                if mismatch :
                        occ.append(i)
        return occ

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def generate (iset) :
        resul = naiv.occ
        for i in iset :
                resul += 1
        return resul

'''genome = readLambdaVirus ('lambda_virus.fa')
genome[:1000]
len(genome)
counts = {'A':0, 'C':0, 'G':0, 'T':0}
for base in genome
        counts[base] += 1
print (counts)

import collections
collections.counter(genome)
'''
