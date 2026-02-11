# level 5
# #21
# number = int(input("Enter a number: "))
#
# if number>=100 and  number <=999:
#     print("its a 3 digit number")
#
# else:
#     print("its not 3 digit  number")
#
# #22
#
# num1 = int(input("Enter a number: "))
# num2 = int(str(num1)[::-1])
# if num1 == num2:
#     print("this is palindrome")
# else:
#     print("it not palindrome")
#
# #23
# name = input("Enter a name: ")
# if name >= "A" and name <= "Z":
#     print("uppercase letter")
# elif name >= "a" and name <= "z":
#     print("lowercase letter")
# elif name >= "0" and name <= "9":
#     print("digit")
# else:
#     print("special character")

#24

experience = int(input("Enter a experience: "))
salary = int(input("Enter a salary: "))

if experience >= 5:
    bonus = salary * 0.2
    print("Your bonus:", bonus)
else:
    bonus = salary * 0.1
print("Your bonus:", bonus)
print("bonus")


#25
pas = input("Enter a password: ")
if len(pas) <= 8:
    print("password is weak")
else:
    print("strong password")


