def boyer_moore (s, p) :
    matches = []
    p_len = len(p)
    p_end = len(p) - 1  #le dernier caractère
    i = j = p_end
    k = 0
    
    while i < len(s) :
        if s[i] == p[j] :
            k = i
            while j > 0 :   #Voir ou le caractère correspond
                i -= 1
                j -= 1
                if s[i] != p[j] :
                    i = k + p_end
                    j = p_end
                    break
                    
            if j == 0 :     #pas de correspondance
                matches.append(i)
                i = k + p_end
                j = p_end
            else :
                try : 
                    m = p.rindex(s[i])  #match position
                    shift = p_end - mpos
                    i += shift
                    continue
                except Error : 
                    i += p_len
                    continue
        return matches

s = 'riobooboobfoboborqdoboohobobbobbboobbobobobobot'
p = 'bob'
print boyer_moore(s, p)
