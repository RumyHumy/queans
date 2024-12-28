#!/usr/bin/python3

import sys
from random import randint

class FileInfo:
    name = None
    obj = None
    data = ''
    entries = []
    def __init__(self, name):
        self.name = name

class State:
    files = [] # FileInfo
    order = 'qa' # qa (question-answer), aq (answer-question), ro (random-order)
    count = None # All
    blur  = None # Shuffle

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
        if   arg in ['-question-answer', '-que-ans', '-qa']:
            State.order = 'qa'
        elif arg in ['-answer-question', '-ans-que', '-aq']:
            State.order = 'aq'
        elif arg in ['-random-order', '-ro']:
            State.order = 'ro'
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
        elif arg[0] == '-':
            print('Unknown "-"-argument')
            exit(1)
        else:
            State.files.append(FileInfo(arg))
        i += 1
    del i

    if len(State.files) == 0:
        print('Files not provided')

    # READ RAW FILES
    #
    class Card:
        content = [] # [question, answer]
    cards = []
    for file in State.files:
        fobj = open(file.name, 'r', encoding='utf-8')
        file.data = fobj.read()
        # Creating backup
        fbak = open(f'{file.name}.bak', 'w', encoding='utf-8')
        fbak.write(file.data)
        fbak.close()
        # Get contents
        file.obj = fobj
        file.entries = file.data.strip().split('\n\n')
        for e in file.entries:
            if e.find('??') > 0:
                card = Card()
                card.content = [c.strip() for c in e.split('??', 1)]
                cards.append(card)
                continue

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

    if State.count == None:
        State.count = len(cards)

    # QUIZ
    #
    print('Les go...\n')
    inv = State.order == 'dt'
    for i, card in enumerate(cards):
        if i > State.count-1:
            break
        if State.order == 'ar':
            inv = randint(0, 1)
        print(card.content[inv])
        input('...')
        print(card.content[1-inv])
        print()
        input()
        print()
