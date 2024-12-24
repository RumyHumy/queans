# termdef
Linux Python script for simple "term-defenition" text quizes

# FILE LAYOUT
```
QUESTION 1:
question??answer

QUESTION 2:
>>>
multiline
question
??
multiline
answer
<<<
```


# OPTIONS
```text
./termdef.py [OPTIONS] <file1> <file2> ... <filen>
-term-def(inition) / -td - asks you term
-def(inition)-term / -dt - asks you defenition
-asks-random / -ar - asks at random term-def/def-term
-single - ask single question
-all    - ask all of the avaliable entries
-count <number-of-questions>
-shuffle, -no-shuffle
-blur <radius> - shuffles nearest in <radius>
```
