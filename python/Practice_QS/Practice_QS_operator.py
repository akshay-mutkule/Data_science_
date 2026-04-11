<<<<<<< HEAD
#Level 1
num = 2
if num>=0:
    print("positive")
else:
    print("negative")


#2

num1 =221
if num1%2==0:
    print("even")
else:
    print("odd")

#3
age = 30
if age >= 18:
    print("you can vote")
else:
    print("you can not vote")

#4
num2 = 45
num3 = 54
if num2>num3:
    print("num2 is greater than num3")
else:
    print("num2 is less than num3")



#5
num4 =44
if num4%5==0:
    print("num4 is divisible by 5")
else:
    print("num4 is not divisible by 5")
#Level 2
# #level 2
#
# #6
#
# marks = 55
# if marks >=40:
#     print("pass")
# else:
#     print("fail")
#
# num1 = 56
# if num1 % 3 ==0 and num1% 7 ==0:
#     print("divisible by 3 and 7")
# else:
#     print("not divisible by 3 and 7")
#
# #8
# year = int(input("Enter year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("leap year")
# else:
#     print("not leap year")
#
# #9
#
# vowel = input("Enter vowel character: ")
# if vowel in ("a","e","i","o","u"):
#     print("vowel character")
# else:
#     print("not vowel character")

#10
age = 70
if age >= 60:
    print("senior citizen")

# Level 3
#level 3

#11

marks = 22
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#12

num1 =3
num2 =6
num3 = 1

if num1> num2 and  num1 > num3 :
    print("num1 is greater ")
elif num2 >num1 and num2 > num3:
    print("num2 is greater ")
else:
    print("num3 is greater")

# 13

num = int(input("Enter a week day: "))
if num == 1:
    print("sunday")
elif num == 2:
    print("monday")
elif num == 3:
    print("tuesday")
elif num == 4:
    print("wednesday")
elif num == 5:
    print("thursday")
elif num == 6:
    print("friday")
elif num == 7:
    print("saturday")

#14

month = int(input("Enter a month: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")

elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
else:
    print("December")

#15
unit = 5
bill = int(input("Enter a unit : "))
print("your bill is: ",unit*bill)




#Level 4

#Level 4

#16
marks = int (input("Enter your marks : "))
if marks >=90:
    print("A","pass")
elif marks >= 75:
    print("B","pass")
elif marks >= 50:
    print("C","pass")
else:
    print("D","Fail")

#17

balance = int (input("Enter your balance : "))
# withdrawl = int (input("Enter your withdrawl : "))
#
# if balance >= withdrawl:
#     print("you can withdrawl")
#     balance -= withdrawl
#     print("your balance is",balance)
# else:
#     print("you can't withdrawl")
#
# #18
#
# username = input ("Enter your username : ")
# passwword = input ("Enter your password : ")
#
# if username == "akshay" and passwword == "123":
#     print("you are logged in")
# else:
#     print("invalid username or password")
#
#
# #19
#
# age = int (input ("Enter your age : "))
# if age <5:
#     print("ticket is free")
# elif age>=5 and age <= 12:
#     print("ticket is 100")
# elif age >=13 and age <= 60:
#     print("ticket is 200")
# elif age >=60 and age <= 120:
#     print("ticket is 300")
# else:
#     print("invalid age")

#20
bill = int(input("Enter your bill: "))

if bill <= 100:
    discount = 0
    print("No discount")

elif bill <= 1000:
    discount = bill * 0.10

else:
    discount = bill * 0.30

print("Your bill is:", bill)
print("Your discount is:", discount)
print("Amount to pay:", bill - discount)

#Level 5

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


#Level 6

# Level 6
# 26

salary = int(input("Enter your salary: "))

if salary <= 10000:
     print("no tax")
elif salary > 10000:
    income =  salary * 12
    tax = income*0.18
    if income > 800000:
        print("you have to pay income tax",tax)
else:
    print("you have to pay income tax")

#27

angle1 = int(input("Enter your angle: "))
angle2 = int(input("Enter your angle: "))
angle3 = int(input("Enter your angle: "))

if angle1 + angle2 + angle3 == 180:
    print("trangle is valid")
else:
    print("invalid trangle")

#28

weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

BMI = (weight / height**2)

if BMI < 20:
    print("you are underweight")
elif 20< BMI < 40:
    print("you are normal")
elif 40< BMI < 100:
    print("you are overweight")
else:
    print("you are not eligible")



#29 Write a program to check eligibility for loan based on salary and credit score.


salary = int(input("Enter your salary: "))
credits = int(input("Enter your credits: "))

if salary > 50000 and  credits > 90:
    print("you are eligible for loan")
else:
    print("you are not eligible for loan")

# Write a program to build a traffic light system.


light = "green"

if light == "green":
     print("go")
elif light == "red":
    print("stop")
elif light == "yrllow":
    print("slow")
else:
    print("wrong color")




#Level 7


salary = int(input("Enter your salary: "))

if salary <= 10000:
     print("no tax")
elif salary > 10000:
    income =  salary * 12
    tax = income*0.18
    if income > 800000:
        print("you have to pay income tax",tax)
else:
    print("you have to pay income tax")

#27

angle1 = int(input("Enter your angle: "))
angle2 = int(input("Enter your angle: "))
angle3 = int(input("Enter your angle: "))

if angle1 + angle2 + angle3 == 180:
    print("trangle is valid")
else:
    print("invalid trangle")







=======
#Level 1
num = 2
if num>=0:
    print("positive")
else:
    print("negative")


#2

num1 =221
if num1%2==0:
    print("even")
else:
    print("odd")

#3
age = 30
if age >= 18:
    print("you can vote")
else:
    print("you can not vote")

#4
num2 = 45
num3 = 54
if num2>num3:
    print("num2 is greater than num3")
else:
    print("num2 is less than num3")



#5
num4 =44
if num4%5==0:
    print("num4 is divisible by 5")
else:
    print("num4 is not divisible by 5")
#Level 2
# #level 2
#
# #6
#
# marks = 55
# if marks >=40:
#     print("pass")
# else:
#     print("fail")
#
# num1 = 56
# if num1 % 3 ==0 and num1% 7 ==0:
#     print("divisible by 3 and 7")
# else:
#     print("not divisible by 3 and 7")
#
# #8
# year = int(input("Enter year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("leap year")
# else:
#     print("not leap year")
#
# #9
#
# vowel = input("Enter vowel character: ")
# if vowel in ("a","e","i","o","u"):
#     print("vowel character")
# else:
#     print("not vowel character")

#10
age = 70
if age >= 60:
    print("senior citizen")

# Level 3
#level 3

#11

marks = 22
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#12

num1 =3
num2 =6
num3 = 1

if num1> num2 and  num1 > num3 :
    print("num1 is greater ")
elif num2 >num1 and num2 > num3:
    print("num2 is greater ")
else:
    print("num3 is greater")

# 13

num = int(input("Enter a week day: "))
if num == 1:
    print("sunday")
elif num == 2:
    print("monday")
elif num == 3:
    print("tuesday")
elif num == 4:
    print("wednesday")
elif num == 5:
    print("thursday")
elif num == 6:
    print("friday")
elif num == 7:
    print("saturday")

#14

month = int(input("Enter a month: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")

elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
else:
    print("December")

#15
unit = 5
bill = int(input("Enter a unit : "))
print("your bill is: ",unit*bill)




#Level 4

#Level 4

#16
marks = int (input("Enter your marks : "))
if marks >=90:
    print("A","pass")
elif marks >= 75:
    print("B","pass")
elif marks >= 50:
    print("C","pass")
else:
    print("D","Fail")

#17

balance = int (input("Enter your balance : "))
# withdrawl = int (input("Enter your withdrawl : "))
#
# if balance >= withdrawl:
#     print("you can withdrawl")
#     balance -= withdrawl
#     print("your balance is",balance)
# else:
#     print("you can't withdrawl")
#
# #18
#
# username = input ("Enter your username : ")
# passwword = input ("Enter your password : ")
#
# if username == "akshay" and passwword == "123":
#     print("you are logged in")
# else:
#     print("invalid username or password")
#
#
# #19
#
# age = int (input ("Enter your age : "))
# if age <5:
#     print("ticket is free")
# elif age>=5 and age <= 12:
#     print("ticket is 100")
# elif age >=13 and age <= 60:
#     print("ticket is 200")
# elif age >=60 and age <= 120:
#     print("ticket is 300")
# else:
#     print("invalid age")

#20
bill = int(input("Enter your bill: "))

if bill <= 100:
    discount = 0
    print("No discount")

elif bill <= 1000:
    discount = bill * 0.10

else:
    discount = bill * 0.30

print("Your bill is:", bill)
print("Your discount is:", discount)
print("Amount to pay:", bill - discount)

#Level 5

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


#Level 6

# Level 6
# 26

salary = int(input("Enter your salary: "))

if salary <= 10000:
     print("no tax")
elif salary > 10000:
    income =  salary * 12
    tax = income*0.18
    if income > 800000:
        print("you have to pay income tax",tax)
else:
    print("you have to pay income tax")

#27

angle1 = int(input("Enter your angle: "))
angle2 = int(input("Enter your angle: "))
angle3 = int(input("Enter your angle: "))

if angle1 + angle2 + angle3 == 180:
    print("trangle is valid")
else:
    print("invalid trangle")

#28

weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

BMI = (weight / height**2)

if BMI < 20:
    print("you are underweight")
elif 20< BMI < 40:
    print("you are normal")
elif 40< BMI < 100:
    print("you are overweight")
else:
    print("you are not eligible")



#29 Write a program to check eligibility for loan based on salary and credit score.


salary = int(input("Enter your salary: "))
credits = int(input("Enter your credits: "))

if salary > 50000 and  credits > 90:
    print("you are eligible for loan")
else:
    print("you are not eligible for loan")

# Write a program to build a traffic light system.


light = "green"

if light == "green":
     print("go")
elif light == "red":
    print("stop")
elif light == "yrllow":
    print("slow")
else:
    print("wrong color")




#Level 7


salary = int(input("Enter your salary: "))

if salary <= 10000:
     print("no tax")
elif salary > 10000:
    income =  salary * 12
    tax = income*0.18
    if income > 800000:
        print("you have to pay income tax",tax)
else:
    print("you have to pay income tax")

#27

angle1 = int(input("Enter your angle: "))
angle2 = int(input("Enter your angle: "))
angle3 = int(input("Enter your angle: "))

if angle1 + angle2 + angle3 == 180:
    print("trangle is valid")
else:
    print("invalid trangle")







>>>>>>> 276650d (files)
