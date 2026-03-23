
print(10+20)
print(10.1)
print(10+2)

number1 = 1234567890
number2 =987654321
print(number1 +number2)
print(number1/number2)

#DataTypes

num = 10  #int
num1 = 10.1  #float
num2  = 3+2j  #complex
bool1 = True

print(type(num))
print(type(num1))
print(type(num2))
print(type(bool1))

#Type casting

num4 = int(num1)
print(type(num4))

#String

str1 ="Hey i am Akshay i am learning python"

print(str1)
print(str1[0])


print(str1[0:3])
print(str1[:])
print(str1[2:])
print(str1[0:-1])
print(str1[-8:])
print(str1[::-1])
print(str1[::2])

#Problem 1
# Write a Python program to print the following:
# Hello World
# Welcome to Python Programming

print("Hello World")
print("Welcome to Python Programming")


# Problem 2
# Print the result of:
num1 = 10 + 5
num2 =10 * 3
num3 = 20 / 4
print(num1)
print(num2)
print(num3)

#problem 3
# Use type() to check the data type of:
num = 25
value = 3.14
str1 = "Python"
type1 = True
print(type(num))
print(type(value))
print(type(str1))
print(type(type1))

# Creating Simple Variables
# Problem 4
# Create variables for:
# your name
# your age
# your city
# Print them in one sentence.
# Example output:
# My name is Rohan, I am 21 years old and I live in Pune.
str2 = "My name is Rohan, I am 21 years old and I live in Pune."
print(str2)


# Problem 5
# Create variables:
a = 10
b = 20
# Print:
# Sum
# Difference
# Product
print(a + b)
print(a>b)


#Rules for Naming Variables
# Problem 6
# Which of the following are valid variable names?
 #1name = 2  this is wrong variable name
name_1 =1  # valid
#student-name =2  this is wrong variable name
totalMarks =3  #valid
_class = 2  #valid


# Write a program that creates three valid variable names and assigns values to them.


# Numeric Data Types
# Problem 7
# Create variables for:
# integer number
# float number
# boolean value
# complex number
# Print their types using type().
num1 = 33
num2 = 34.4
num4 = True
num_3 = 4+6j
print(type(num1))
print(type(num2))
print(type(num4))
print(type(num_3))


#Problem 8
# Create:
a = 5
b = 2.5
c = True
d = 3 + 4j
# Print each variable and its type.
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)

#Sequence Types Strings

# Problem 9
# Create a string:
text = "Python Programming"
# Print:
# First character
# Last character
# Length of the string
# Lists
print(text[0])
print(text[-1])
print(len(text))
print(list(text))


#Problem 10
# Create a list:
numbers = [10, 20, 30, 40, 50]
# Print:
# First element
# Last element
# Length of list
# Tuples
print(numbers[0])
print(numbers[1])
print(len(numbers))
print(tuple(numbers))


#Problem 11
# Create a tuple:
colors = ("red", "green", "blue")
# Print:
# First color
# Total number of colors
print(colors[0])
print(len(colors))

#Type Casting

# Problem 12
# Convert:
num = 10
# to:
# float
# string
# Print the result and type.
print(type(float(num)),num)
print(type(str(num)),num)

# #Problem 13
# Convert the string "50" into an integer and add 25.
# Expected output:
# 75
str1 = "50"
num1 =(int(str1))
print(num1+25)


#Strings (Indexing & Slicing)

# Problem 14
word = "Python"
# Print:
# First letter
# Third letter
# Last letter
print(word[0])
print(word[2])
print(word[-1])

#
# Problem 15
# From the string:
text = "DataScience"
# Print:
# Data
# Science
print(text[0:4])
print(text[4:])

#String Methods

# Problem 16
text = "python programming"
# Convert it to:
# Uppercase
# Capitalize
# Title case
text2 = text.upper()
text3 = text.lower()
text4 = text.title()
print(text2)
print(text3)
print(text4)


#Problem 17

text = "   Hello Python   "
print(text)
# Remove extra spaces using string method.
text1 = text.strip()
print(text1)


#String Concatenation

# Problem 18
# Create:
first = "Data"
second = "Science"
# Join them using concatenation.
# Expected output:
# Data Science
str1 = first +" "+ second
print(str1)





