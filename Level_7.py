
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
