#!/usr/bin/python3

import sys
from random import randint

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments')
        exit(1)

    # Read raw
    file = open(sys.argv[1], 'r', encoding='utf-8')
    cards = [c.split('??') for c in file.read().split('\n') if '??' in c]
    file.close()

    # Shuffle
    for i in range(len(cards)):
        p1, p2 = i, randint(0, len(cards)-1)
        cards[p1], cards[p2] = cards[p2], cards[p1]

    inv = '--inverse' in sys.argv[1]
    for card in cards:
        if len(card) < 2:
            print('Error. No term')
            break
        print(card[inv])
        ans = input('Press Enter if ready...').lower()
        print(card[1-inv])
        print()
        # get it?
