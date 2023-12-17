Simple question selector based on the weightage of your desired exam.
I mainly created it for JEE mains and Advanced exams for Indian students.
You can create your own custom CSV file and use it.

The program gives output in two ways-No. of questions to be attempted per
chapter and a randomised question no. list.
The resources I used while preparing were often ordered in 
increasing order of difficulty.Exams are a mix of both easy and tough question types
so I made the randomiser to simulate a question paper.Ideally you should be able to program 
the no. of easy, medium and difficult questions too, but this was good enough for me, for the moment.

The CSV file format should be as follows:
Chapter, Percentage
Chapter_1,5
.
.
.

Make sure that
1) chapter names don't have commas in their name (if they are remove them
As I typed this I realised that I gave a very poor explanation for the reason I made this
, When practicing questions,I often have to calculate how many questions I have to do per chapter I decide to do on that particular day.
Not all chapters have equal importance and it would be dumb to do equal no. of questions from each chapter.
So I made this as I found calculating how many questions to do per chapter ,a tedious exercise.


HOW IT WORKS

1)You decide which subject you want to study.
2)You either edit the program to include the CSV file path ,if u are going to do this frequently or simply give the program the file path
3)The program gives you the List of subjects and their respective weightage.
4)You tell the program
a)How many chapters you want to practice
b)The no. of questions you want to practice
c)The name of the chapter
d)How many questions you have in your question bank or resource (remember the randomiser will give you a no. between 1 and this no.)
e)Do the same for other chapters

And you are done.

You will receive how many questions you need to do based on the importance of the chapter.


TO BE IMPROVED
1)Instead of a randomiser, You could get a distribution containing easy, medium and difficult questions
2)The go back option doesn't work perfectly.It should go back one step instead of several.
3)The weightage is rounded off to get questions in integers rather than fractions.This leads to the program sometimes giving a no. +1 or -1 than the requested no..
4)When all chapters are requested,You currently need to enter all the chapter names manually.

That are all I can think of for now
