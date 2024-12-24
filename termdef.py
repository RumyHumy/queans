#!/usr/bin/python3

import sys
from random import randint

class State:
    fnames = []
    order = 'td' # td (term-def), dt (def-term), ar (asks-random)
    count = None # All
    blur  = None # Complete randomness
    use_score = True

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
        if   arg in ['-term-def', '-term-definition', '-td']:
            State.order = 'td'
        elif arg in ['-def-term', '-definition-term', '-dt']:
            State.order = 'dt'
        elif arg in ['-asks-random', '-ar']:
            State.order = 'ar'
        elif arg in ['-single']:
            State.count = 1
        elif arg in ['-all']:
            State.count = None
        elif arg in ['-shuffle']:
            State.blur = None
        elif arg in ['-no-shuffle']:
            State.blur = 0
        elif arg in ['-count']:
            i += 1
            narg = subarg(i, arg)
            if not narg.isnumeric():
                wrong_subarg(arg)
            State.count = int(narg)
        elif arg in ['-blur']:
            i += 1
            narg = subarg(i, arg)
            if not narg.isnumeric():
                wrong_subarg(arg)
            State.blur = int(narg)
        elif arg in ['-score']:
            State.use_score = None
        elif arg in ['-no-score']:
            State.use_score = 0
        elif arg[0] == '-':
            print('Unknown "-"-argument')
            exit(1)
        else:
            State.fnames.append(arg)
        i += 1
    del i

    if len(State.fnames) == 0:
        print('Files not provided')

    # READ RAW FILES
    #
    class Card:
        content = None
        fname = None
        bline = None
        eline = None
        score = None
    exit()

    # SHUFFLE
    #
    for i in range(len(cards)):
        p1 = i
        if State.blur == None:
            p2 = randint(0, len(cards)-1)
        else:
            p2 = i+randint(-State.blur, +State.blur)
            p2 = max(0, min(p2, len(cards)-1))
        cards[p1], cards[p2] = cards[p2], cards[p1]

    # SORT BY SCORE
    #
    #cards.sort(key=lambda x: x.score, reverse=True)

    # QUIZ
    #
    print('Les go...')
    inv = State.order == 'dt'
    for i, card in enumerate(cards):
        print(card.content, card.score)
        if i > State.count-1:
            break
        if State.order == 'ar':
            inv = randint(0, 1)
        print(card.content[inv], end='')
        input('...')
        print(card.content[1-inv], end='')
        if State.use_score == True:
            if card.score == None:
                card.score = 0
            score = input('Good/Weak/Bad (g/w/B): ').lower()
            score = 1 if score == 'g' else 0 if score == 'w' else -1
            card.score = min(0, card.score+score)
        print()
