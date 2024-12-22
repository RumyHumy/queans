# termdef
Python script for simple "term-defenition" text quizes

# FILE LAYOUT
```
question??answer

>>>
multiline
question
??
multiline
answer
<<<
```


# OPTIONS:
./termdef.py <file1> <file2> ... <filen> [OPTIONS]
--term-def(inition)/--td - asks you term
--def(inition)-term/--dt - asks you defenition
--asks-random/--ar - asks at random
--single - ask single question
--all    - ask all of the avaliable entries
--count <number-of-questions>
--shuffle, --no-shuffle
--blur <radius-of-blur>
