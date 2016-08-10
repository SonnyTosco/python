# Given the following list:
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# # Create a program that outputs:
# # Michael Jordan
# # John Rosales
# # Mark Guillen
# # KB Tonel
# for x in students:
#     print x['first_name'], x['last_name']
#
# Now given the following dictionary:
# users = {
#  'Students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
# for x in users:
#     counter=0
#     print x
#     for y in users[x]:
#         counter+=1
#         name=y['first_name'].upper()+" "+y['last_name'].upper()
#         length=len(y['first_name'])+len(y['last_name'])
#         print "{}-{}-{}".format(counter, name, length)
