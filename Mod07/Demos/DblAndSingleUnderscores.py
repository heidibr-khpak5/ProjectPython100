# ----------------------------------------------------------------------------------------------------------------- #
# Title: Demo - Double vs Single Underscores
# Description: Demonstrates how to use Double vs Single Underscores in classes.
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ----------------------------------------------------------------------------------------------------------------- #

""" Most advance programing languages offer the ability to control access to class fields and attributes.
Python, does as well, but in an unusual way that allows developers to decide when to ignore this control """

# Demo 1: Simple Class Fields
class JustFields:
    _file_name = 'single_test.txt'
    __file_name = 'double_test.txt'


# Use case 1: Reading from fields
# print(JustFields._file_name)  # Python does give you a warning "Access to a protected member _file_name of a class"
# print(JustFields.__file_name)  # Python hides double underscore fields from read access and throws an error if you try using it.
# print(JustFields._JustFields__file_name)  # However, you can still read its data using its "Mangled" name!
# print(JustFields._JustFields_file_name)  # Note that the single underscore names do not get "Mangled" names.


# Use case 2: Writing to fields
# JustFields._file_name = 'single'
# JustFields.__file_name = 'double'  # Oddly, Python adds new field to class if you try to write to the dbl underscore fields!
#
# print(JustFields._file_name)
# print(JustFields.__file_name)
# print(JustFields._JustFields__file_name)


# Demo 2: Object Attributes

class WithAttributes:

    def __init__(self, file_name):
       self._file_name = file_name
       self.__file_name = file_name


# Use case 1: Reading from attributes
# wa_obj = WithAttributes('test.txt')
# print('single: ', wa_obj._file_name)  # Once again, Python lets you read the single underscore directly.
#
# try:
#     print('double: ', wa_obj.__file_name)  # but throws an error reading the double underscore directly and no warning.
# except Exception as e:
#     print(e)
#
# print('Mangled: ', wa_obj._WithAttributes__file_name)  # Though you can still get at it using the "Mangled" name.


# Use case 2: Writing to Attributes
# wa_obj = WithAttributes('test.txt')
# wa_obj._file_name = 'single'  # Sadly, single underscore attribute are NOT write protected
# print('single: ', wa_obj._file_name)
#
# wa_obj.__file_name = 'double'  # and neither are double underscore attributes...
# print('double: ', wa_obj.__file_name)
#
# wa_obj._WithAttributes__file_name = 'double'  # nor the "mangled" ones!
# print('Mangled: ', wa_obj._WithAttributes__file_name)


# Conclusion:
# * Use __ if you want at least some enforcement
# * Use _ if you want at to alert other developer, but with no enforcement
# * Use just a regular name if you don't want any enforcement or alerts
# * Use properties if you want to add validation logic and formatting