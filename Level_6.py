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




