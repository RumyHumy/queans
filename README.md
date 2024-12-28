# termdef
CLI linux Python script for simple "question-answer" text quizes

# FILE LAYOUT
```
QUESTION 1:

que??ans


QUESTION 2:

2+2??4


QUESTION 3:

do you like your life?
??
yeah
```

# OPTIONS
```text

./termdef.py [OPTIONS] <file1> <file2> ... <filen>

CARDS ORDER:
-shuffle, -no-shuffle
-blur <radius> - shuffles nearest in <radius>

QUESTIONING ORDER:
-question-answer / -qa - normal questioning order
-answer-question / -aq - inverse questioning order
-random-order / -ro    - random questioning order

AMOUNT:
-single - ask single question
-all    - ask all of the avaliable entries
-count <number-of-questions>
```
