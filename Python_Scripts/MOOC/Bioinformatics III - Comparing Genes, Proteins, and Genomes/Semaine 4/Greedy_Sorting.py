#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

from operator import neg


def greedy_sorting(permutation):
    '''A greedy algorithm to sort by reversals.'''

    # Initialiser une liste pour stocker.
    permutation_sequence = []

    # Fonction Lambda pour trouver l'index d'un élément donné dans la permmutation.
    k_index = lambda perm, k: map(abs, perm).index(k)

    # Fonction Lambda pour échanger et annuler la région
    k_sort = lambda perm, i, j: perm[:i] + map(neg, perm[i:j+1][::-1]) + perm[j+1:]

    # Boucle sur la permutation pour trier.
    i = 0
    while i < len(permutation):
        if permutation[i] == i+1:
            i += 1
        else:
            permutation = k_sort(permutation, i, k_index(permutation, i+1))
            permutation_sequence.append(permutation)

    return permutation_sequence


def main():
    with open('data/Greedy_Sorting.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

    # Obtenir la liste des recerals.
    reversal_list = greedy_sorting(perm)

    reversal_list = ['('+' '.join([['', '+'][value > 0] + str(value) for value in perm])+')' for perm in reversal_list]

    # Print and save the answer.
    print '\n'.join(reversal_list)
    with open('Data/Greedy_Sorting_An.txt', 'w') as output_data:
        output_data.write('\n'.join(reversal_list))

if __name__ == '__main__':
    main()
