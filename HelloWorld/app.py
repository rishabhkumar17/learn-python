# print("Hello World!")

# variables
# age = 20
# price = 17.07
# first_name = "sage"
# is_online = False
# print(age, price, first_name, is_online)

# Receiving Input
# name = input("What is your name? ")
# print("Hello " + name)

# Type Conversion
# birth_year = input("Enter your Birth Year: ")
# age = 2023- int(birth_year)
# print(age)

# int()
# float()
# bool()
# str()

# a = input("First: ")
# b = input("Second: ")
# print("sum: ", float(a) + float(b))
# print("sum: " + str(float(a) + float(b)))

# Strings
# course = "python for sage"
# print(course.upper())
# print(course.lower())
# print(course.find('y'))
# print(course.replace('for', '4'))
# print('python' in course)

# Arithmetic Operators
# print(10 + 7)
#
# print (10 / 7)
# print(10 // 7)
# print(10 % 7)
# print(10 ** 7)
#
# x = 10
# x += 7
# print(x)

# Operator Precedence
# x = (10 + 3) * 2
# print(x)

# Comparison Operator
# x = 3 > 2
# >=
# <=
# ==
# !=
# <
# >
# print(x)

# Logical Operators
# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)

# If Statements
# temperature = 7
# if temperature > 30:
#     print("Hot day!")
# elif temperature > 20:
#     print("Nice day!")
# elif temperature > 10:
#     print("Bit cold!")
# else:
#     print("Cold day!")
# print("Done!")

# Exercise
# weight = input("Weight: ")
# unit = input("(K)g | (L)bs: ")
# if unit.upper() == "K":
#     converted = float(weight) // 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = float(weight) * 0.45
#     print("Weight in Kgs: " + str(converted))

# while loop
# i = 1
# while i <= 1_00:
#     print(i * "*")
#     i += 1

# Lists
# names = ["sage", "johan", "ten-ma", "shinichi"]
# print(names[0])
# print(names[-1])
# names[0] = "savage"
# print(names[0])
# print(names[0:3])

# List Methods
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# print(numbers)
# numbers.insert(0, -1)
# # numbers.clear()
# print(1 in numbers)
# print(len(numbers))

# for loop
# numbers = [1, 2, 3, 4, 5, 6, 7]
# for item in numbers:
#     print(item)

# range() function
# numbers = range(1, 8, 2)
# for number in numbers:
#     print(number)
#
# for number in range(8):
#     print(number)

# tuples -> immutable object
numbers = (1, 2, 3, 7, 7)
# numbers[0] = 0 # error
numbers.count(7)  # return 2

