#!/usr/bin/env python
'''
Developer: Christian Nazili - Universite de Namur, Namur, Belgium
'''

def dp_change(money, coins) :
    min_coins = [0]+[(money/min(coins))+1]*money

    for i in xrange(1, money+1) :
        for coin in coins :
            if i >= coin :
                if min_coins[i-coin] + 1 < min_coins[i] :
                    min_coins[i] = min_coins[i-coin] +1
    return min_coins[money]

def main() :
    with open('Data/Dp_change.txt') as input_data :
        money = int(input_data.readline().strip())
        coins = map(int, input_data.readline().strip().split(','))

    min_number = str(dp_change(money, coins))
    print min_number

    with open('Data/Answer/Dp_change.txt','w') as output_data :
        output_data.write(min_number)

if __name__ == '__main__' :
    main()
