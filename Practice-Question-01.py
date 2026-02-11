#1. Temperature Conversion: Convert 98.6°F to Celsius using: C = (F - 32) × 5/9

import math
temp = 98.6
celsius = (temp -32)*5/9
print(celsius)
print()
#2. Circle Calculations: Calculate area and circumference of a circle with radius 7.5 cm

radius =float(7.5)
area = 3.14*(radius**2)
print(area)


circumference = 2*(math.pi*radius)
print(circumference)

print()
#3 BMI Calculator: Calculate BMI for weight=68kg, height=1.75m (BMI = weight/height²)


bmiw = 68
bmih = 1.7
BMI = (bmiw/bmih**2)
print(BMI)


print()
#4 Time Converter: Convert 5678 seconds to hours, minutes, and remaining seconds
time = 5678

hrs = time //3600
print(hrs)
p = 5678-3600
print(p)
2078
min = 2078//60
print(min)

sec = 2078%60
print(hrs,"hrs",min, "min",sec,"sec")

#5 Compound Interest: Calculate final amount for ₹5000 at 8% annual interest for 3 years: A = P(1 + r/100)^t

rs = 5000
cp = 5000*(1 + 8/100)**3
print(cp)

#Logical operator

#6 Eligibility Check: Check if a person aged 22 with 85% marks is eligible for a job (age≥21 and marks≥80)

age = 22
marks = 85
if(age >= 22):
    if(marks == 85):
        print("you are eligible for job")
else:
    print("you are not eligible for job")

#7 Discount Eligibility: Check if a customer with ₹2500 purchase on a weekend gets 15% discount (purchase≥2000 or weekend=True)

cust = int(2500)
weekend = True
print(cust >=2000 and weekend == True)



#8 Login System: Validate username="admin" and password="12345" or recovery_email=True

username = "admin"
password = int(12345)
recovery_mail = True

valid = (username=="admin" and password==12345 or recovery_mail == True)
print("vadil credential: ", valid)


#9 Grade Check: Student passes if (attendance≥75 and marks≥40) or medical_excuse=True

attendence = 80
marks = 45
medical_execuse = True
if(attendence >=75 and marks >=40 or medical_execuse ==True):
    print("student passes")
else:
    print("student Fails")


#10  Triangle Validator: Check if sides 7, 10, 5 can form a triangle (sum of any two > third)

A = 7
B = 10
C = 5
if(A+B >=C or B+C >=A or C+A >=B):
    print("Trangle Validate")


# Mixed operations


#11        Number Properties: For number 29, check if it's positive, even, and divisible by 3

num = 29
print("positive number",num >=0)
print("even number:", num%2 ==0)
print("odd number:", num%3==0)

# 12. Leap Year Checker: Check if 2024 is a leap year (divisible by 4 and not by 100,  unless also divisible by 400)

year = 2024
print("divisible by 4 number:", num%4 ==0 and num%100 !=0)
print("divisible by 400 number:", num%400 ==0)

#13. Shipping Cost: Calculate cost: ₹50 base + ₹20/kg for weight>5kg, with 10% discount for online orders

weight = 10
online = True



#14. Data Usage: Calculate remaining data from 10GB plan after using 2.3GB, 1.7GB, and 0.8GB

