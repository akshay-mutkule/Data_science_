# Operator

num =10
num1 = 20

print("add :",num+num1)
print("sub :",num-num1)
print("mul :",num*num1)
print("div :",num/num1)
print("exponent:",num**num1)
print("Floor division :",num//num1)
print("mod :",num%num1)

# Comparison Operator

num2 = 10
num3 = 30
print("Greater than:",num2>num3)
print("Less than:",num2<num3)
print("greater than equal to:",num2>=num3)
print("less than equal to:",num2<=num3)
print("Equal to:",num2==num3)
print("Not equal to:",num2!=num3)


#Assignment Operator

num4 = 10
num4 += 20
print(num4)

num4-=20
print(num4)

num4 /=20
print(num4)

num4 *=20
print(num4)


#Logical Operator

num5 = 20
num6 = 40

print(num5<num6 and num5<num6)
print(num5>num6 or num5<num6)
print(not num5> num6)


#if Condition
age = 18
if age > 18:
    print("valid age to vote")
else:
    print("invalid age to vote")


#elif

age = 65
if age > 18 and age <60:
    print("valid age to vote")
elif age >60:
    print("age for retirement")
else:
    print("invalid age to vote")

num = 10
num1 = 20
num2 =40

if num> num1 and num> num2:
    print("num is greater ")

elif num1 > num and num1 > num2:
    print("num1 is greater ")
else:
    print("num2 is greater ")


# Part 1: Arithmetic Operators
# Q1
#
# Write a program that takes two numbers from the user and prints:
#
# Addition
#
# Subtraction
#
# Multiplication
#
# Division

nums = int(input("Enter a number: "))
nums1 = int(input("Enter a number: "))

addi = nums+nums1
print(addi)
div = nums/num1
print(div)
mod = num%num1
print(mod)
mul = num*num1
print(mul)
sub = num-num1
print(sub)

