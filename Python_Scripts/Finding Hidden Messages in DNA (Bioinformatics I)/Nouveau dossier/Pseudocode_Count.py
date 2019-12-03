def Pattercount (t, p) :
	count = 0
	for i in range (len(t)- len (p)) :
		if t(i, len(p)) = p :
			count += 1
	return count
