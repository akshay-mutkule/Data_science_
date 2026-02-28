# Syntax Error
#print("Hello World"

#Lgical Error
print(3+2*7)
print(3*2+7)

# print(10/0)
#Exception Handling

try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("Division by zero is not allowed")

try:
    x = int("ABC")
except Exception as e:
    print("Error Occured ",e)
    # Finally:   Always Run
finally:
    print("End of the program")


age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Your age cannot be negative")
print("age is Valid")





