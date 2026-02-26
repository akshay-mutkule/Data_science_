  # Polymorphism
  # poly-many,morophism-forms

class Animal:
    def speaks(self):
        print("Animal Speaks")
class Dog:
    def speaks(self):
        print("Dog barks")
class Cat:
    def speaks(self):
        print("Cat Meaww")

a = Animal()
b = Dog()
c = Cat()

a.speaks()
b.speaks()
c.speaks()


class Payment:
    def pay(self):
        print("payment")
class Card(Payment):
    def pay(self):
        print("card payment")
class UPI(Payment):
    def pay(self):
        print("UPI payment")

p = Payment()
c = Card()
u = UPI()

p.pay()
c.pay()
u.pay()



# Inheritance

#child can access there parent class properties

#single Inheritance
class Parent:
    def skills(self):
        print("Drives")
class Child(Parent):
    def studies(self):
        print("Studies")

c = Child()
c.skills()
c.studies()


print("---------multilevel Inheritance---------")
#MultiLevel Inheritance

class GrandParent:
    def show(self):
        print("Farming")

class Parent(GrandParent):
    def skills(self):
        print("Drives")
class Child(Parent):
    def studies(self):
        print("Studies")

c = Child()
p = Parent()

p.skills()
c.show()

c.show()
c.studies()
c.skills()



print("---------multiple Inheritance---------")


class Mother:
    def skill1(self):
        print("cooking")
class Father:
    def skill2(self):
        print("Driving")
class Child(Mother,Father):
    def skill3(self):
        print("inherit")

c = Child()

c.skill1()
c.skill2()
c.skill3()


#Hieerarchical Inheritane
print("---------Hirarchical Inheritance---------")

#
# class Prarent:
#     def skill1(self):
#         print("pk")
# class child1(Prarent):
#     def skill2(self):
#         print("pk2")
# class child2(Prarent):
#     def skill3(self):
#         print("pk3")
#
# c = child1()
# c.skill1()
#
# c1 = child2()
# c1.skill2()



# Hybrid Inheritance
print("-------------Hybrid Inheritance---------")

class Grandparents:
      def skill1(self):
            print("Grandparents")
class Parents(Grandparents):
    def skill2(self):
        print("Parents")
class Child1(Parents):
    def skill3(self):
        print("Child1")
class Child2(Parents):
    def skill4(self):
        print("Child2")
class Child3(Parents):
    def skill5(self):
        print("Child3")

c = Child3()
c.skill1()
c.skill2()

c1 = Child1()
c1.skill1()
c1.skill2()



# Encapsulation

# private Variable

# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance
#     def set__balance(self,amount):
#         if amount<0:
#             print("Invalid Input")
#         else:
#             self.__balance += amount
#
#     def get__balance(self):
#         return self.__balance
# Account = Bank(20000)
# print(Account.get__balance())
# Account1 = Bank(10000)
# print(Account1.get__balance())

#
# class Bank:
#     def __init__(self,name,balance):
#         self.__name = name
#         self.__balance = balance
#     def set__balance(self,amount):
#         if amount<0:
#             print("Invalid Input")
#         else:
#             self.__balance += amount
#     def withdraw(self. amount):
#     if amount < 0:
#             print("Invalid Input")
#
#     def get__balance(self):
#         return self.__balance
# Account = Bank(20000)
# print(Account.get__balance())
# Account1 = Bank(10000)
# print(Account1.get__balance())


# Abstraction

from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Ford(Car):
    def start(self):
        print("car Started")
    def stop(self):
        print("car stopped")
c1 = Ford()
c1.start()
c1.stop()
