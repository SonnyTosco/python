def multiply (a,var):
    b=[]
    for i in a:
        i=i*var
        b.append(i)
    return b
a=[2,4,10,16]
b=multiply(a,5)
print b
