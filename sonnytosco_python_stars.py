# Create a function called draw_stars() that take a list of numbers and prints out *
# For example: x=[4,6,1,3,5,7,25]
# draw_stars(x) should print the following in when invoked:
# ****
# ******
# *
# ***
# *****
# *******
# *********************************
def draw_stars (a,var):
    b=[]
    for i in a:
        i=i*var
        b.append(i)
    return b
a=[2,4,10,16]
for i in draw_stars(a,'*'):
    print i

# Modify the function above. Allow a list containing integers and strings to be passed
# to the  draw_stars() function. When a string is passed, instead of  displaying *,
# display the first letter of the string according to the example below.
# You may use the .lower() string method for this part.

# For example:
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj

y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
def draw_stars2(my_list):
    for item in my_list:
        output = ''
        if type(item) is int:
            for i in range(item):
                output += '*'
        elif type(item) is str:
            first_letter = item[0].lower()
            for i in range(len(item)):
                output += first_letter
        print output

draw_stars2(y)
