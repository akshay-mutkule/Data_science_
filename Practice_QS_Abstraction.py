# Use from abc import ABC, abstractmethod
#
# 🚗 Car Abstraction
# 6️⃣ Vehicle System
#
# Create abstract class Vehicle:
#
# abstract method start()
#
# abstract method stop()
#
# Create:
#
# Car class
#
# Bike class
#
# Implement both methods differently

from abc import ABC, abstractmethod

class Vehicle(ABC):


    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car engine started with key")

    def stop(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike start")

    def stop(self):
        print("Bike stop")

car = Car()
bike = Bike()

car.start()
car.stop()

print("---------------")

bike.start()
bike.stop()


print("---------------")


#7

from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class ElectricCar(Car):
    def drive(self):
        print("Electric car engine driving")

    def fuel_type(self):
        print("Electric car engine fuel type")


class PetrolCar(Car):
    def drive(self):
        print("Petrol car engine driving")

    def fuel_type(self):
        print("Petrol car engine fuel type")


#create obj

ele = ElectricCar()
petrol = PetrolCar()

ele.drive()
ele.fuel_type()
petrol.drive()
petrol.fuel_type()

print("--------------------------")
#8

from abc import ABC, abstractmethod


# Abstract Class
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# Implementing Class
class BankATM(ATM):

    def __init__(self, balance):
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.__balance


# Testing
atm = BankATM(10000)

atm.deposit(2000)
atm.withdraw(5000)
print("Current Balance:", atm.check_balance())

print("-----------------------")
#9

from abc import ABC, abstractmethod


# Abstract Class
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


# SBI ATM Implementation
class SBI_ATM(ATM):

    def withdraw(self, amount):
        print(f"SBI ATM: ₹{amount} withdrawn successfully.")


# HDFC ATM Implementation
class HDFC_ATM(ATM):

    def withdraw(self, amount):
        print(f"HDFC ATM: Please collect your ₹{amount} cash.")


# Testing
sbi = SBI_ATM()
hdfc = HDFC_ATM()

sbi.withdraw(5000)
hdfc.withdraw(3000)