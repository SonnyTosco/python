# You're going to create a program that simulates tossing a coin 5,000 times.
# Your program should display how many times the head/tail appears.
#
# Sample output should be like the following:
#
#           Starting the program...
#
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far

def cointoss():
    import random
    random_num=random.random()
    x_rounded=round(random_num)
    if (x_rounded == 0):
        return "heads"
    if(x_rounded == 1):
        return "tails"
count=0
head=0
tails=0
for count in range (0,5000):
    a=cointoss()
    if (a=="heads"):
        head+=1
    else:
        tails+=1
    count+=1
    print "Throwing a coin. It's {}. Got {} heads so far and {} tails so far.".format(a, head, tails)
print "Ending the program, thank you!"
