# termdef
CLI linux Python script for simple "question-answer" text quizes

# EXAMPLES
In order quiz
```console
./queans.py -no-shuffle test.txt
```

Single question
```console
./queans.py -single test.txt
```

Answer-question quiz
```console
./queans.py -aq test.txt
```

Both ways quiz
```console
./queans.py -ro test.txt
```

A little bit of shuffle
```console
./queans.py -blur 2 test.txt
```

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
