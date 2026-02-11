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

