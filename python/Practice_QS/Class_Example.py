<<<<<<< HEAD
# object = real world entity
#class = is used to define the object

class Student:
#constructor
   def __init__(self,name ,age, marks,email,roll_no):
       self.name =name
       self.age = age
       self.marks = marks
       self.email = email
       self.roll_no = roll_no

   def display(self):
    print("name:",self.name)
    print("age: " ,self.age)
    print("marks: ",self.marks)
    print("email:",self.email)
    print("roll no:",self.roll_no)

s1 = Student("akshay",21,99,"akshay@344",32)
s1.display()


class Car:

    def __init__(self,car,model,hp,color,logo):
        self.car =car
        self.model = model
        self.hp =hp
        self.color = color
        self.logo = logo

    def show(self):
        print(self.car)
        print(self.model)
        print(self.hp)
        print(self.color)
        print(self.logo)

f1 = Car("RRR","4m",55665,"blue","stylish")
f1.show()

=======
# object = real world entity
#class = is used to define the object

class Student:
#constructor
   def __init__(self,name ,age, marks,email,roll_no):
       self.name =name
       self.age = age
       self.marks = marks
       self.email = email
       self.roll_no = roll_no

   def display(self):
    print("name:",self.name)
    print("age: " ,self.age)
    print("marks: ",self.marks)
    print("email:",self.email)
    print("roll no:",self.roll_no)

s1 = Student("akshay",21,99,"akshay@344",32)
s1.display()


class Car:

    def __init__(self,car,model,hp,color,logo):
        self.car =car
        self.model = model
        self.hp =hp
        self.color = color
        self.logo = logo

    def show(self):
        print(self.car)
        print(self.model)
        print(self.hp)
        print(self.color)
        print(self.logo)

f1 = Car("RRR","4m",55665,"blue","stylish")
f1.show()

>>>>>>> 276650d (files)
