# Create a program that prompts the user ten times for a test score between 60 and 100.
# Each time a score is generated, your program should display what is the grade of
# that score. Here is the grade table:
def grades(a):
        if(a<60):
            print "Study harder"
        elif (a>59 and a<70):
            print "Score is {}; Your grade is a D.".format(a)
        elif (a>69 and a<80):
            print "Score is {}; Your grade is a C.".format(a)
        elif (a>79 and a<90):
            print "Score is {}; Your grade is a B.".format(a)
        elif (a>89 and a<=100):
            print "Score is {}; Your grade is an A.".format(a)
count=0
for count in range(0,10):
    print 'What was your grade?'
    a=input()
    grades(a)
    count+=1
print "End of the program. Bye!"
