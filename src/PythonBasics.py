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

# match - cases are an alternative control structure that is more efficient 
# when it comes to matching single strings
DRILLING_ID = 'D_06'

match DRILLING_ID:
    case 'D_00':
        print(f'the drilling {DRILLING_ID} encountered {weathering_grades[2]} rock')
    case 'D_01':
        print(f'the drilling {DRILLING_ID} encountered {weathering_grades[1]} rock')
    case _:
        print('unknown drilling')


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

# Exercise 5

fibonaccis = [0]

running_number = 1

STOP = 200

while running_number < STOP:
    fibonaccis.append(running_number)
    running_number = fibonaccis[-1] + fibonaccis[-2]

print(fibonaccis)


# for loop
# for loops are there to iterate over finite numbers of elements

soiltype_list = ['silt', 'sand', 'cobbles', 'clay', 'silty clay', 'sandy silt']
soil_cohesions = [10, 0, 0, 30, 20, 5]

for i in range(len(soiltype_list)):
    print(soiltype_list[i], soil_cohesions[i])

# Exercise 6
STOP = 1000

numbers = []

for i in range(STOP):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
print(sum(numbers))


# Exercise 7


rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
         'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
         'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke',
         'suevite']

year = 2007

years = list(range(year, year + len(rocks)))

# for loop approach 1
for i in range(len(rocks)):
    print(f'the rock of the year {years[i]} was {rocks[i]}')

# for loop approach 2
for i, rock in enumerate(rocks):
    print(f'the rock of the year {years[i]} was {rock}')

# for loop approach 3
for rock, year in zip(rocks, years):
    print(f'the rock of the year {year} was {rock}')

# Exercise 3 bonus:

# create a new empty list

empty_list = []

# compute the number of characters of the strings 'marl', 'gneiss', 'limestone', 'eclogite'

rocks = ['marl', 'gneiss', 'limestone', 'eclogite']

# append the numbers to the empty list in the above given order

for rock in rocks:
    n_characters = len(rock)
    empty_list.append(n_characters)

# print the list

print(empty_list)

# compute the sum of the last three elements of the list

sum_of_last_3 = sum(empty_list[-3:])

# print the result as a string “the result is: XX” two times by using the .format() method and an f-string.

print(f'the result is: {sum_of_last_3}')


# Exercise 8

# create two lists with the following content:
rock_list = ['gneiss', 'marl', 'limestone']
ucs = [150, 45, 90]

# create a dictionary called “rock_dict” with the first list as keys and the 
# second list as values

rock_dict = dict(zip(rock_list, ucs))

# add a new entry to the dictionary consisting of a new rock type and an 
# according UCS value

rock_dict['dolomite'] = 120

# print the content of the whole dictionary to the console through formatted
# strings saying “The XX has a UCS of YY MPa”. Use a for-loop for this

for rock in rock_dict.keys():
    print(f'The {rock} has a UCS of {rock_dict[rock]} MPa.')


# Exercise 9

# compute the mean value, the median, the variance and the standard deviation
# for that list: 
c = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

# print the results with values rounded to 2 digits

# mean
mean_value = sum(c) / len(c)
print(f'mean value: {round(mean_value, 2)}')

# median
c = sorted(c)

if len(c) % 2 == 0:  # in case of an even list
    mid_upper = int(len(c) / 2)  # first we get the upper index
    mid_lower = mid_upper - 1  # then we get the lower index
    median = (c[mid_upper] + c[mid_lower]) / 2
else:  # in case of an uneven list
    mid = int(len(c) / 2)
    median = c[mid]

print(f'median value: {round(median, 2)}')

# variance
sum_list = []

for x_i in c:
    sum_list.append((x_i - mean_value)**2)

sum_of_sum_list = sum(sum_list)

variance = sum_of_sum_list / len(c)

print(f'variance value: {round(variance, 2)}')

# standard deviation
standard_deviation = variance**0.5

print(f'standard deviation: {round(standard_deviation, 2)}')





###########################
# session 3 on 17. September 2025
###########################

# 1. repetition

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
