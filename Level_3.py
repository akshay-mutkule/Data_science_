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




