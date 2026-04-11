<<<<<<< HEAD
#PART 1: Basic Try–Except Practice
#1 Simple Division Program
# Write a program that:
#
# Takes two numbers from the user
#
# Divides them
#
# Handles:
#
# ZeroDivisionError
#
# ValueError
try:
   num1 = int(input("Enter a number: "))
   num2 = int(input("Enter another number: "))
   result = num1/num2
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")

#2
# Convert Input to Integer
#
# Write a program that:
#
# Takes user input
#
# Converts it to an integer
#
# If the user enters text, print:
# "Please enter a valid number"

try:
    num3 = input("Enter a number: ")
    num4 = int(num3)
    print(num4)
except ValueError:
    print("Invalid input please enter a number")

#3 Access List Element

# Create a list:
# numbers = [10, 20, 30, 40, 50]
# Write a program that:
#Asks the user to enter an index
# Prints the element at that index
# Handles IndexError
try:
    numbers = [10, 20, 30, 40, 50]
    insert = int(input("Enter a number: "))
    print("Your index element is :", numbers[insert])
except IndexError:
    print("Index out of range")

#4 String + Number Error
# Write a program that
# Adds a number and a string
# Handles TypeError
# Prints a friendly message

try:
    num3 = int(input("Enter a number: "))
    str1 = str(input("Enter a string: "))
    print(num3+str1)
except TypeError:
    print("its not possible to concate str or int")

#5Multiple Exceptions

# Write a small calculator that:
# Takes two numbers from the user
# Divides them
# Handles:
# ValueError
# ZeroDivisionErro

try:
    num5 = int(input("Enter a number: "))
    num6 = int(input("Enter another number: "))
    print(num5/num6)
except ZeroDivisionError:
    print("it cant Divisible by zero")
except ValueError:
    print("Invalid input")

#  PART 2: Basic raise Practice

#6  Age Validation

# Write a program that:
#
# Takes age as input
#
# If age < 0 → raise ValueError("Age cannot be negative")

try:
   age = int(input("Enter a number: "))
   if age<0:
       raise ValueError("Your age cannot be negative")
   print(age,"is valid")
except ValueError:
   print("your age is not become -ve")


#7 Marks Validation
# Write a program that:
# Takes marks as input
# If marks < 0 or marks > 100 → raise ValueError

try:
    marks = int(input("Enter a number: "))
    if marks < 0:
        raise ValueError("Your marks cannot be negative")
    print(marks,"is valid")
except Exception as e:
    print("generic error",e)


#8 Password Length Check
# Write a program that:
# Takes password from the user
# If password length < 6 → raise an error


try:
    pas = int(input("Enter a number: "))
    if pas.length < 6:
        raise ValueError("Your passage cannot be less than 6")
    print(pas,"is valid")
except Exception as e:
    print("generic error",e)

#  PART 3: Using finally
# 9  Basic Finally Example
#
# Write a program that:
#
# Takes a number
#
# Divides 100 by that number
#
# Uses finally to print:
# "Program Finished"

try:
    num7 = int(input("Enter a number: "))
    mock = 100/num7
    print(mock,"is valid")
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program finishd")

#10 File Example
# Write a program that:
# Opens a file
# Reads its content
# Uses finally to print:
# "File operation -"


# try:
#     with open("Practice_QS_operator.py", "r") as file:
#         content = file.read()
#         print("File Content:")
#         print(content)
# except FileNotFoundError:
#     print("File not found.")


try:
    file = open("Practice_QS_operator.py", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found.")











#11
# Safe Input Program
# Write a program that:
# Keeps asking the user for a numbe
# Stops only when a valid number is entered
# Uses try–except

while True:
    try:
        num = float(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
=======
#PART 1: Basic Try–Except Practice
#1 Simple Division Program
# Write a program that:
#
# Takes two numbers from the user
#
# Divides them
#
# Handles:
#
# ZeroDivisionError
#
# ValueError
try:
   num1 = int(input("Enter a number: "))
   num2 = int(input("Enter another number: "))
   result = num1/num2
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")

#2
# Convert Input to Integer
#
# Write a program that:
#
# Takes user input
#
# Converts it to an integer
#
# If the user enters text, print:
# "Please enter a valid number"

try:
    num3 = input("Enter a number: ")
    num4 = int(num3)
    print(num4)
except ValueError:
    print("Invalid input please enter a number")

#3 Access List Element

# Create a list:
# numbers = [10, 20, 30, 40, 50]
# Write a program that:
#Asks the user to enter an index
# Prints the element at that index
# Handles IndexError
try:
    numbers = [10, 20, 30, 40, 50]
    insert = int(input("Enter a number: "))
    print("Your index element is :", numbers[insert])
except IndexError:
    print("Index out of range")

#4 String + Number Error
# Write a program that
# Adds a number and a string
# Handles TypeError
# Prints a friendly message

try:
    num3 = int(input("Enter a number: "))
    str1 = str(input("Enter a string: "))
    print(num3+str1)
except TypeError:
    print("its not possible to concate str or int")

#5Multiple Exceptions

# Write a small calculator that:
# Takes two numbers from the user
# Divides them
# Handles:
# ValueError
# ZeroDivisionErro

try:
    num5 = int(input("Enter a number: "))
    num6 = int(input("Enter another number: "))
    print(num5/num6)
except ZeroDivisionError:
    print("it cant Divisible by zero")
except ValueError:
    print("Invalid input")

#  PART 2: Basic raise Practice

#6  Age Validation

# Write a program that:
#
# Takes age as input
#
# If age < 0 → raise ValueError("Age cannot be negative")

try:
   age = int(input("Enter a number: "))
   if age<0:
       raise ValueError("Your age cannot be negative")
   print(age,"is valid")
except ValueError:
   print("your age is not become -ve")


#7 Marks Validation
# Write a program that:
# Takes marks as input
# If marks < 0 or marks > 100 → raise ValueError

try:
    marks = int(input("Enter a number: "))
    if marks < 0:
        raise ValueError("Your marks cannot be negative")
    print(marks,"is valid")
except Exception as e:
    print("generic error",e)


#8 Password Length Check
# Write a program that:
# Takes password from the user
# If password length < 6 → raise an error


try:
    pas = int(input("Enter a number: "))
    if pas.length < 6:
        raise ValueError("Your passage cannot be less than 6")
    print(pas,"is valid")
except Exception as e:
    print("generic error",e)

#  PART 3: Using finally
# 9  Basic Finally Example
#
# Write a program that:
#
# Takes a number
#
# Divides 100 by that number
#
# Uses finally to print:
# "Program Finished"

try:
    num7 = int(input("Enter a number: "))
    mock = 100/num7
    print(mock,"is valid")
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program finishd")

#10 File Example
# Write a program that:
# Opens a file
# Reads its content
# Uses finally to print:
# "File operation -"


# try:
#     with open("Practice_QS_operator.py", "r") as file:
#         content = file.read()
#         print("File Content:")
#         print(content)
# except FileNotFoundError:
#     print("File not found.")


try:
    file = open("Practice_QS_operator.py", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found.")











#11
# Safe Input Program
# Write a program that:
# Keeps asking the user for a numbe
# Stops only when a valid number is entered
# Uses try–except

while True:
    try:
        num = float(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
>>>>>>> 276650d (files)
        print("Invalid input! Please enter a valid number.")