def readFASTQ(filename):    
    f = open(filename)
    reads = []
    while True:
        h = f.readline()
        if len(h) == 0:
            break
        sequence = f.readline().rstrip()
        _ = f.readline()
        quality = f.readline().rstrip()
        reads.append(sequence)
        
    return reads

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def pick_maximal_overlap(reads, k):
    """ Return a pair of reads from the list with a
        maximal suffix/prefix overlap >= k.  Returns
        overlap length 0 if there are no such overlaps."""
    reada, readb = None, None
    best_olen = 0
    
    kmer_dict = {}
    
    for read in reads:
        for i in range(len(read)-k+1):
            kmer_dict[read[i:i+k]] = set()
            
    for read in reads:
        for i in range(len(read)-k+1):
            kmer_dict[read[i:i+k]].add(read)
   
    for read in reads:
        current_kmer_set = kmer_dict[read[-1*k:]]
        for kmer_read in current_kmer_set:
            if read != kmer_read:
                olen = overlap(read, kmer_read, min_length=k)                
                if olen > best_olen:
                    reada, readb = read, kmer_read
                    best_olen = olen
    return reada, readb, best_olen
    
def greedy_scs(reads, k):
    """ Greedy shortest-common-superstring merge.
        Repeat until no edges (overlaps of length >= k)
        remain. """
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

