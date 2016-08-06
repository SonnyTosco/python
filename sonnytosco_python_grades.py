# Create a program that prompts the user ten times for a test score between 60 and 100.
# Each time a score is generated, your program should display what is the grade of
# that score. Here is the grade table:

def grades(a):
    a=input()
    if(a<60):
        print "Study harder"
    else:
        if(a>59 or a<70):
            print "Score is {}; Your grade is a D.".format(a)
        else:
            if(a>69 or a<80):
                print "Score is {}; Your grade is a C.".format(a)
            else:
                if(a>79 or a<90):
                    print "Score is {}; Your grade is a B.".format(a)
                else:
                    if(a>89 or a<=100):
                        print "Score is {}; Your grade is an A.".format(a)
