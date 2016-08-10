# Creating Modules
# Since arithmetic is another python file saved in the same folder we can
# call the function from that file and use it in this file using import.

# import arithmetic
# print arithmetic.add(5,8)
# print arithmetic.subtract(10,5)
# print arithmetic.multiply(12,6)

# Packages
# - a module is a single file (or files) that are imported under one import.
# A package is a collection of modules in directories that give a package hierarchy.
#
# from my_package.subdirectory import my_functions
#
# Writing Packages
# - each package in python is a directory which mUST contain a special file called
# __init__.py. This file can be empty, and it indicates that the directory containing
# it is a Python package, so it can be imported the same way a module can be imported.
#
# If we create a directory called my_modules, which marks the package name,
# we can then create a module inside that package called test_module. We also
# must not forget to add the __init__.py file inside the my_modules directoryself.
#
# To use the module test_module, we can import it in two ways:
# import my_modules.test_module OR from my_modules import test_module
#
# The __init__.py file can also decide which modules this package will export
# as an API, while keeping other modules internal by overriding the __all__ variable, like so:
# __init__.py:
# __all__ = ["test_module"]
