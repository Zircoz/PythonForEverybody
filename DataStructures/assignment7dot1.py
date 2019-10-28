'''
WAP that prompts for a file name,then opens that file and reads through the file,and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.

Expected output -->
WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE
AND REWARDING ACTIVITY  YOU CAN WRITE PROGRAMS FOR
MANY REASONS RANGING FROM MAKING YOUR LIVING TO SOLVING
A DIFFICULT DATA ANALYSIS PROBLEM TO HAVING FUN TO HELPING
SOMEONE ELSE SOLVE A PROBLEM  THIS BOOK ASSUMES THAT
{\EM EVERYONE} NEEDS TO KNOW HOW TO PROGRAM AND THAT ONCE
YOU KNOW HOW TO PROGRAM, YOU WILL FIGURE OUT WHAT YOU WANT
TO DO WITH YOUR NEWFOUND SKILLS

WE ARE SURROUNDED IN OUR DAILY LIVES WITH COMPUTERS RANGING
FROM LAPTOPS TO CELL PHONES  WE CAN THINK OF THESE COMPUTERS
AS OUR PERSONAL ASSISTANTS WHO CAN TAKE CARE OF MANY THINGS
ON OUR BEHALF  THE HARDWARE IN OUR CURRENT-DAY COMPUTERS
IS ESSENTIALLY BUILT TO CONTINUOUSLY AS US THE QUESTION
WHAT WOULD YOU LIKE ME TO DO NEXT

OUR COMPUTERS ARE FAST AND HAVE VASTS AMOUNTS OF MEMORY AND
COULD BE VERY HELPFUL TO US IF WE ONLY KNEW THE LANGUAGE TO
SPEAK TO EXPLAIN TO THE COMPUTER WHAT WE WOULD LIKE IT TO
DO NEXT IF WE KNEW THIS LANGUAGE WE COULD TELL THE
COMPUTER TO DO TASKS ON OUR BEHALF THAT WERE REPTITIVE
INTERESTINGLY, THE KINDS OF THINGS COMPUTERS CAN DO BEST
ARE OFTEN THE KINDS OF THINGS THAT WE HUMANS FIND BORING
AND MIND-NUMBING
'''

#Words.txt is as follows:
'''
Writing programs or programming is a very creative
and rewarding activity  You can write programs for
many reasons ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem  This book assumes that
{\em everyone} needs to know how to program and that once
you know how to program, you will figure out what you want
to do with your newfound skills

We are surrounded in our daily lives with computers ranging
from laptops to cell phones  We can think of these computers
as our personal assistants who can take care of many things
on our behalf  The hardware in our current-day computers
is essentially built to continuously ask us the question
What would you like me to do next

Our computers are fast and have vasts amounts of memory and 
could be very helpful to us if we only knew the language to 
speak to explain to the computer what we would like it to 
do next If we knew this language we could tell the 
computer to do tasks on our behalf that were reptitive  
Interestingly, the kinds of things computers can do best
are often the kinds of things that we humans find boring
and mind-numbing
'''

#Code:

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip().upper()
    print(line)
