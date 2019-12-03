#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def naive_aligment(p, t) :
    appat = []
    ali = 0
    for i in range(len(t) - len(p) +1) :
        ali += 1
        for j in range (len(p)) :
            match = True
            if t[i+j] != p[j] :
                match = False
                break
        if match == True
            appat.append(i)
    return appart, ali
 
 """pour naive_comparaison
    meme code, sauf mettre la deuxième boucle avant le ali+=1
    puis meme chose"""