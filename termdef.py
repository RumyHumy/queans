#!/usr/bin/python3

# OPTIONS:
# File can be provided at any place
# --term-def(inition)/--td, --def(inition)-term/--dt, --random-order/--ro
# --single - ask single question
# --all    - ask all of the avaliable entries
# --count <number-of-questions>

import sys
from random import randint

class State:
    fnames = []
    order = 'td' # td, dt, ro
    count = None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments')
        exit(1)

    # READ ARGS
    #
    def wrong_subarg(arg):
        print(f'Wrong subarg for "{arg}"')
        exit(1)
    def subarg(i, arg):
        if i >= len(sys.argv):
            print(f'Subargument expected for "{arg}"')
            exit(1)
        return sys.argv[i]
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if   arg in ['--term-def', '--term-definition', '--td']:
            State.order = 'td'
        elif arg in ['--def-term', '--definition-term', '--dt']:
            State.order = 'dt'
        elif arg in ['--random-order', '--ro']:
            State.order = 'ro'
        elif arg in ['--single']:
            State.count = 1
        elif arg in ['--all']:
            State.count = None
        elif arg in ['--count']:
            i += 1
            narg = subarg(i, arg)
            if not narg.isnumeric():
                wrong_subarg(arg)
            State.count = int(narg)
        elif arg[:2] == '--':
            print('Unknown "--"-argument')
            exit(1)
        else:
            State.fnames.append(arg)
        i += 1
    del i

    if len(State.fnames) == 0:
        print('Files not provided')

    # READ RAW FILES
    #
    cards = []
    for fname in State.fnames:
        file = open(fname, 'r', encoding='utf-8')
        for c in file.read().split('\n'):
            if '??' in c:
                cards.append(c.split('??'))
        file.close()

    # SHUFFLE
    #
    for i in range(len(cards)):
        p1, p2 = i, randint(0, len(cards)-1)
        cards[p1], cards[p2] = cards[p2], cards[p1]

    # QUIZ
    #
    inv = '--inverse' in sys.argv[1]
    for i, card in enumerate(cards):
        if i == State.count-1:
            break
        if len(card) < 2:
            print('Error. No term')
            break
        print(card[inv])
        print('-')
        ans = input('Press Enter...').lower()
        print('-')
        print(card[1-inv])
        print()
        # get it?
