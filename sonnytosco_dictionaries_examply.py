# Creating dictionaries
# When you initially create a dictonary, it is very much like making a tuple or listself.
# Dictionaries use "{}"

# weekend = { "Sun": "Sunday", "Mon": "Monday" } #literal notation
# vals = dict(one=1, two=2) # dict() function
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# d = { i: object() for i in range(4) } #dictionary comprehension
#
# Above the dictionaries were created in four different ways:
# - literal notation. Key value pairs are enclosed by curly brackets. The pairs are
# seperated by commas The first value of a pair is a key, which is followed by a colon
# character and a value. The "Sun" string is a key and the "Sunday" string is a value.
# - using the dict() function
# - creating an empty dictionary and then, adding some values. The keys inside are
# inside the square brackets, the values are located on the right side of the argument.
# - using a dictionary comprehension. The comprehension has two parts. The first part is the i:
# object() expression, which is executed for each cycle of a loop. The second part is:
# for i in range (4) loop. The dictionary comprehension creates a dictonary having
# four pairs, where the keys are numbers 0,1,2,3 and the values are simple objects.

# Using for loops to access all keys and values:
#to print all keys
# for data in capitals:
#      print data
# #another way to print all keys
# for key in capitals.iterkeys():
#      print key
# #to print the values
# for val in capitals.itervalues():
#      print val
# #to print all keys and values
# for key,data in capitals.items():
#      print key, " = ", data

# Built-in Functions and Methods
# Python includes the following standalone functions for dictionaries:
#
# cmp(dict1, dict2) - compares elements of both dictionaries.
# len() - give the total length of the dictionary.
# str() - produces a printable string representation of a dictionary.
# type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.

# Python includes the following dictionary methods:
# (either dict.method(yourDictionary) or yourDictionary.method() will work)
#
# .clear() - removes all elements from the dictionary
# .copy() - returns a shallow copy dictionary
# .fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
# .get(key, default=None) - For key key, returns value or default if key is not in dictionary.
# .has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
# .items() - returns a list of dictionary's (key, value) tuple pairs.
# .keys() - return a list of dictionary keys.
# .setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
# .update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
# .values() - returns list of dictionary values.

# Nested dictionaries
# Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples.
# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }
# for key, data in context.items():
#      #print data
#      for value in data:
#           print "Question #", value["id"], ": ", value["content"]
#           print "----"

# Lists from dictionary
# It's possible to create lists from dictionaries by using the methods items(),
# keys(), and values(). As the name implues the method keys() creates a list,
# which consists solely of the keys of the dictionary. While values() produces a list
# consisting of the values. Items() can be used to create a list consisting of 2-tuples of
# (key-value)-pairs:

# data ={"house":"Haus","cat":"Katze","red":"rot"}
# print data.items()
# #[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
# print data.keys()
# #['house', 'red', 'cat']
# print data.values()
# #['Haus', 'rot', 'Katze']

# Dictionaries from lists
# Example: we have two lists, one containing the dishes and the other,
# the corresponding countries.
#
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]

# Now we will create a dictionary, which assigns a dish to a country
# (of course according to the common prejudices). For this purpose, we need the
# function zip(). The name zip was well chosen because the two lists get combined
# like a zipper.
# country_specialities = zip(countries, dishes)
# print country_specialities

# The variable "country_specialties" contains now the dictionary in the 2-tuple
# list form. This form can be easily transformed into a real dictionary with the
# function dict().
# country_specialities_dict = dict(country_specialities)
# print country_specialities_dict
