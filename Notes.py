# import random  # This should be on line 1
# # This is working
# # print("Hello World")
#
# # Alberto
#
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print# this makes a new line. In python 3.6, it looks like: print()
# print("See if you can figure this out")
# print (14%5)
#
# car_name = "Wiebe Moblie"
# car_type = "Lambrogini Sesta Elemento"
# car_cylinders = 8
# car_mpg= 9000.1
#
# # Inline printing
# # print("I have a car called the %s" % car_name)
# # print(
#
#
#
#
#
#
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
# print_hw()
# print_hw()
#
#
# def say_hi(name):
#     print("Hello %s." % name)
#     print("Enjoy your day")
#
#
# say_hi("John")
#
# def print_age(name, age):
#     print("%s is %d years old." % (name, age))
#     age += 1 # age = age + 1
#     print("Next year, they will be %d" % age)
#
#
# print_age("John", 15)
#
# def f(x):
#     return x**3 + 4 * x**2 + 7 * x - 4
#
#
# print(f(3))
# print(f(4))
# print(f(5))
#
#
# # If statement
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "b"
#     elif percentage >= 70:
#         return "c"
#     elif percentage >= 60:
#         return "d"
#     elif percentage <= 50:
#         return "f"
#
#
# def happy_bday(name):
#     print("Happy birthday to you" + "'")
#     print("Happy birthday to you" + "'")
#     print("Happy birthday to "+ name + "'")
#     print("Happy birthday to you" + "'")
#
#
# happy_bday("John")
#
#

# lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "Soda"]

print(shopping_list[2])

print(len(shopping_list))

# Goimg through a list
for item in shopping_list:
    print(item)

for number in the_count:
    print(number * 2)

len(shopping_list)
# Gives me the length of the list
range(3)


# gives length of the number 0 through 2
range (len(shopping_list))

for number in range(len(shopping_list)):
    item = shopping_list[number]
    print("The at index %d is %s" % (number, item))
# turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))
# Add thing to a list
shopping_list.append("cereal")
shopping_list.append("soap")
print(shopping_list)
# removing things from shopping list
shopping_list.remove("Soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class

import string
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
# Dictionaries - Made up of Key: Value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'OH': 'Ohio'
}

print(large_dictionary['FL'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacramento',
        'Los Angeles'
    ],
    'FL': [
        "Tampa",
        "Orlando",
        "Miami"
    ],
    'OH': [
        "Cleavland",
        "Cincinnati",
    ]
}

print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])


largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}
current_node = largest_dictionary['AZ']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])
