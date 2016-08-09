# Tuple Basics
# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# julia=julia[:3]+("Eat Pray love", 2010)+julia[5:]
# print julia

# Tuple Assignments
# value=("Michael", "Instructor", "Coding Dojo")
# (name, position, company)=value
# print name
# print position
# print company

# Built-In Tuple Functions
# len() returns the number of items in a sequence
# tuple_data=('physics', 'chemistry', 1997,2000)
# print len(tuple_data)

# max() returns the maximum item in the sequence
# tuple_data=('physics', 'chemistry', 'x-ray', 'python')
# tuple_num=(67,89,31,15)
# print max(tuple_data)
# print max(tuple_num)

# min() returns the minimum item in the sequence
# tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
# tuple_num = (67, 89, 31, 15)
# print min(tuple_data)
# print min(tuple_num)

# sum() sums the individual items
# tuple_num = (67, 89, 31, 15)
# print sum(tuple_num)

# any() return true if there exists any item in the tuple which is true.
# If a tuple contained (0, False,",0.0,[]), all of which have boolean types of false,
# then any (tuple) would be false. If a tuple contained [-1,-2,10,-4,40], all of
# which evaluate to True, then any(tuple) would be true.
# tuple_num = (67, 89, 31, False, 0, None)
# print any(tuple_num)
#
# all() return true if all items are true
# tuple_num = (67, 89, 31, False, 0, None)
# print all(tuple_num)

# enumerate() iterate through the tuple returning 2-tuples of (index, item).
# This function "enumerates" all the items in a sequence: it provides a
# number and each element of the original sequence in a 2-tuple.
# num = (1, 5, 7, 3, 8)
# for index, item in enumerate(num):
#     print(str(index)+" = "+str(item))
#result is...
#0 = 1
#1 = 5
#2 = 7
#3 = 3
#4 = 8

# sorted() iterate through the tuple in sorted order. Note: the returned
# collection is a sorted list, not a tuple.
# num = (1, 5, 7, 3, 8)
# print sorted(num)
#result: [1,3,5,7,8]

# reversed() iterate through the tuple in reverse order. Note that th return value
# from reversed() is generic <reversed object> and must be fed into the tuple() or
# list() constructor to create one of those objects.
# num = (9, 1, 8, 2, 7, 3)
# print tuple(reversed(num))
#result: (3, 7, 2, 8, 1, 9)

# Tuples as return values
# Functions can always only return a single value,
# but by making that value a tuple, we can effetively grou together as many values
# as we like, and return them together. This is very useful- we often want to know some
# highest and lowest score, or we wat to find the mean and the standard deviation,
# or we want to know the year, the month, and the day.
# For example, we could write a function that returns both the circumference
# and the area of a circle of radius r:
# def get_circle_area(r):
#     #Return (circumference, area) of a circle of radius r
#     c = 2 * math.pi * r
#     a = math.pi * r * r
#     return (c, a)
