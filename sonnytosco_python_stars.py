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
def multiply (a,var):
    b=[]
    for i in a:
        i=i*var
        b.append(i)
    return b
a=[2,4,10,16]
b=multiply(a,'*')
print b
