#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Préfixe 0 et ajoutez len(permutation) +1 pour vérifier si les points finaux sont en place
    return sum(map(lambda x,y: x - y != 1, permutation+[len(permutation)+1], [0]+permutation))


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Lire les données
    with open('Data/Breakpoint.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

    num_of_breakpoints = breakpoint_count(perm)

    # Print and save the answer.
    print str(num_of_breakpoints)
    with open('Data/Breakpoint_An.txt', 'w') as output_data:
        output_data.write(str(num_of_breakpoints))

if __name__ == '__main__':
    main()
