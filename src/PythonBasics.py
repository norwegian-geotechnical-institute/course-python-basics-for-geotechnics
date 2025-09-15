# -*- coding: utf-8 -*-
"""
Script for the "Python Basics" part of the
"Fundamentals of Machine Learning in Geotechnics" course that is helf for
PWD Malaysia in September 2025 by the Norwegian Geotechnical Institute.

This script contains the code that was written during the course
The code is for educational purposes only.
All content of the repository falls under the MIT-license -> see license file.

Author: Dr. Georg H. Erharter, georg.erharter@ngi.no
"""

###########################
# session 1 on 15. September 2025
###########################

### introduction and overview


### general notes

# to comment things out in VSCode use "ctrl + k + c"
# to uncomment things in VSCode use "ctrl + k + u"


### basic datatypes: strings, integers, floats, print function

# there are 2 ways to create strings:
'Hello world'  # single quote string
"Hello world"  # double quote string
# ... and both can be used to create multi line strings with linebreaks
"""
Hello
World
"""

'''
Hello
World
'''

# integers = numbers without decimals
1, 2, 3

# floats = floating point numbers = numbers with decimals
1.2, 34.6789, 100.100

# the print() function is used to print output and results to the console
print('Hello World')

# there are functions to convert datatypes into each other
print(float(10))
print(int(10.734))
print(str(10))

# Exercise 1

### operators: +, -, /, *, **, //, %

# addition
print(1 + 3)

# subtractions
print(54 - 98)

# division
print(10 / 3)

# multiplication
print(12*12)

# to the power of
print(3**3)

# floored division
print(10 // 3)

# modulo
print(10 % 3)

# Exercise 2

# 5 to the power of 8
print(5**8)
# square - root of 9
print(9**(1/2))
# remainder of 14 / 5
print(14 % 5)
# product of the floored quotient of 13 and 3 with 3
print(13//3*3)


### variables, string formatting

# give meaningful variable names
n_outcrops = 4

# string formatting is used to create dynamic strings and there are multiple
# options

# string concatenation
output_string_0 = 'today I mapped ' + str(n_outcrops) + ' outcrops'

# .format() method
output_string_1 = 'today I mapped {} outcrops'.format(n_outcrops)

# f-string method
output_string_2 = f'today I mapped {n_outcrops} outcrops'

print(output_string_0)
print(output_string_1)
print(output_string_2)

# typical use case for string formatting: file path creation
# here we use a "fromatted raw" string so that the backslashes are ignored
filename = 'figure3'
filepath = fr'C:\Users\GEr\{filename}.jpg'
print(filepath)

# dir function to see methods of objects
print(dir(123.34))


### datatypes: lists, tuples, dictionaries, indices, exceptions / errors

# from start       0       1         2         3
# from end        -4      -3        -2        -1
soiltype_list = ['silt', 'sand', 'cobbles', 'clay', 'silty clay', 'sandy silt']
print(soiltype_list)

# accessing single elements
print(soiltype_list[2])

# slicing of lists
print(soiltype_list[:3])
print(soiltype_list[3:])
print(soiltype_list[2: 4])

# lists can be modified e.g. by adding or inserting values
soiltype_list.append('gravel')
soiltype_list.insert(1, 'silty sand')

# len() gives us the number of elements of a list, tuple or string
print(len(soiltype_list))

# lists can be concatenated with +
example_list_1 = [1, 2, 3, 4]
example_list_2 = [5, 6, 7, 8]
concatenated_list = example_list_1 + example_list_2

# lists can be multiplied with *
multiplied_list = concatenated_list * 10


# the range() function can be used to create a range of numbers
# range() by default creates a range of numbers starting from 0 up to the
# entered number at a step of 1. But start, stop and step can be modified
print(list(range(2, 100, 4)))


# # Exercise 3

# create a new empty list
x = []

# compute the number of characters of the strings 'marl', 'gneiss', 'limestone', 'eclogite'
# append the numbers to the empty list in the above given order
x.append(len('marl'))
x.append(len('gneiss'))
x.append(len('limestone'))
x.append(len('eclogite'))

# print the list
print(x)

# compute the sum of the last three elements of the list
sum_last_3 = sum(x[-3:])

# print the result as a string “the result is: XX” two times by using the .format() method and an f-string.
print('the result is: {}'.format(sum_last_3))
print(f'the result is: {sum_last_3}')


# tuples are also collections of objects, but they cannot be modified
example_tuple = (10, 20, 30, 40)
print(example_tuple)
# to modify a tuple, convert it to another datatype first
example_tuple = list(example_tuple)
example_tuple.append(50)
print(example_tuple)
# ... and then convert it back
example_tuple = tuple(example_tuple)
print(example_tuple)


# a dictionary is an unordered collection of pairs of keys and values
# keys must be unique, values can be anything
#                      keys          values

friction_angle_dict = {'clay': [20, 19, 21],
                       'sand': [28, 29, 30],
                       'gravel': [35, 34, 33]}

print(friction_angle_dict['sand'])

# new entries can be added to the dictionary like this
friction_angle_dict['silt'] = [22, 23, 24]

# dictionaries can be created from lists
rocks = ['marl', 'limestone', 'granite']
UCSs = [30, 120, 200]  # [MPa]

rock_UCS_dcit = dict(zip(rocks, UCSs))

print(rock_UCS_dcit)

# keys and values of dictionaries can be accessed directly
soils = list(friction_angle_dict.keys())
friction_angles = list(friction_angle_dict.values())

### control structures: conditional statements: if, elif, else, operators

# control structures help to either avoid or repeat certain parts of code
# conditional statements make use of operators to compare if certain conditions
# are True or False

rock_strength = 176  # MPa

if rock_strength > 50 and rock_strength <= 100:
    print('this is a moderately strong rock')
elif rock_strength > 100 and rock_strength <= 200:
    print('this is a hard rock')
elif rock_strength > 200:
    print('this is a very strong rock')
else:
    print('this is a soft rock')

# types of operators

# >
print(8 > 9)

# >=
print(8 >= 8)

# == 
print(7 == 7)

# <
print(7 < 8)

# <=
print(7 <= 7)


### control structures: loops: while loop, for loop
# loops are used to repeat parts of code

# while loop is a loop that runs until a condition is not True anymore

STOP_CRITERION = 10

iterator = 0

while iterator < STOP_CRITERION:
    print(f'this is iteration number: {iterator}')
    # iterator = iterator + 1
    iterator += 1

print(f'now the loop is finished because the iterator = {iterator}')



###########################
# session 2 on 16. September 2025
###########################

# 1. Repetition


# 2. new topics in accition to yesterday

# list concatenation with +
# range()
# == vs is 
# != vs is not
# match cases

















# Exercise 5

# Exercise 6

# Exercise 7


# Exercise 3 bonus:


###########################
# session 3
###########################

# Exercise 8

# Exercise 9

### functions

# Exercise 10


### coding style, Zen of Python


###########################
# session 4
###########################


### modules, code environments, module documentation


# exercsie 11

# exercsie 12

# exercsie 13
