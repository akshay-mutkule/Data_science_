#List

lst = [10,20,30,40,50,60]
print(lst)


list1 = [10, "akshay", 10.2, 32]
print(list1)
print(list1[1])
print(list1[-1])
print(list1[1:])
print(list1[1:3])


shopping = ["Bread","Butter"]
print(shopping)
shopping.append("Milk")

shopping.extend(["Eggs","Banana","Orange juice"])
print(shopping)

shopping.insert(1,"Apple")
print(shopping)

shopping.remove("Apple")
print(shopping)

shopping.pop()
print(shopping)

shopping.reverse()
print(shopping)

shopping.clear()
print(shopping)

list2 = [10,20,30,40,50,20,20,60,70,80]
print(list2)
print(list2.index(50))
print(list2.count(20))

list2.sort()
print(list2)

list2.reverse()
print(list2)


# Tuple

tup = (10,20,30,40,20,20,50,60)
print(tup)

tup1 = (10,)
print(type(tup1))

print(tup[3])
print(tup[1:-1])
print(tup.index(10))
print(tup.count(20))

# 🔹 Part 1: Understanding Lists
# Q1
#
# Create a list of 5 fruits and print the list.
list = ["apple","mango","banana","custord Apple","orange"]
print(list)
#
# Q2
#
# Create a list of 5 numbers and print:
#
# first element
#
# last element
list1 = [1,2,3,4,5]
print(list1)
# Q3
#
# Create a list:
#
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
# Print the third element.
#
# 🔹 Part 2: Indexing and Slicing
# Q4
#
# Given:
#
numbers = [10,20,30,40,50,60]
#
# Print:
#
# first 3 elements
#
# last 2 elements
print(numbers[0:3])
print(numbers[-2:])
# Q5
#
# Create a list of 10 numbers and print elements from index 3 to 7.
list2 = [1,2,34,5,5,6,7,8,85,8,5]
print(list2[3:8])
# Q6
#
# Given:
#
colors = ["red","blue","green","yellow","black"]
#
# Print:
#
# first color
#
# last color using negative indexing
print(colors[0])
print(colors[-1])
# 🔹 Part 3: List Methods
# append()
# Q7
list5 = ["Apple","orange"]
list5.append("mango")
print(list5)
# Create a list of fruits and add "mango" using append().
#
# extend()
# Q8
#
# Create two lists:
#
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)
#
# Combine them using extend().
#
# insert()
# Q9
#
# Insert "orange" at index 2 in a fruit list.
list6 = ["Apple","mango"]
list6.insert(2,"mango")
print(list6)
list6.remove("mango")
print(list6)
# remove()
# Q10
#
# Remove "banana" from this list.
#
fruits = ["apple","banana","mango"]
# pop()
# Q11
#
# Remove the last element from a number list using pop().
#
# clear()
# Q12
#
# Create a list of numbers and remove all elements using clear().
#
# index()
# Q13
#
# Find the index position of "mango".
#
# count()
# Q14
#
# Count how many times 2 appears in this list.
#
# numbers = [1,2,3,2,4,2]
# sort()
# Q15
#
# Sort this list.
#
# numbers = [5,3,8,1,9]
# reverse()
# Q16
#
# Reverse the list.
#
# numbers = [1,2,3,4,5]
# 🔹 Part 4: Grocery List Program
# Q17
#
# Write a program that:
#
# Creates an empty grocery list
#
# Adds milk, bread, eggs
#
# Prints the list
#
# Q18
#
# Modify grocery list:
#
# add butter
#
# remove bread
#
# print final list
#
# 🔹 Part 5: Tuple Practice
# Q19
#
# Create a tuple with 5 numbers and print it.
#
# Q20
#
# Access the second element of a tuple.
#
# Q21
#
# Try to change a value in a tuple and observe the error.
#
# Example:
#
# t = (10,20,30)
# t[0] = 100
#
# Explain why the error occurs.
#
# 🔹 Part 6: List vs Tuple Practice
# Q22
#
# Create:
#
# list1 = [1,2,3]
# tuple1 = (1,2,3)
#
# Add an element to the list and try to add an element to the tuple.
#
# Observe the difference.
#
# Q23
#
# Convert a tuple into a list.
#
# Q24
#
# Convert a list into a tuple.
#
# 🔹 Part 7: Small Real Programs
# Q25
#
# Write a program to store 5 student names in a list and print them.
#
# Q26
#
# Write a program to:
#
# store 10 numbers
#
# sort them
#
# print highest number
#
# Q27
#
# Create a tuple storing days of the week and print them.
#
# ⭐ Bonus Challenge
# Q28
#
# Create a program where user enters 5 grocery items and store them in a list.
#
# Q29
#
# Count how many times a specific item appears in the list.
#
# Q30
#
# Sort the grocery list alphabetically.
#
