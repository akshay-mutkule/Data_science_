#q1

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("deposit successful",amount)

        else:
            print("deposit failed")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdraw successful",amount)
        else:
            print("withdraw failed")

    def get_balance(self):
        return self.__balance

acc1 = BankAccount(1000)

acc1.deposit(100)
acc1.withdraw(200)
print("current balance :",acc1.get_balance())

acc1.withdraw(2000)

print("---------------------------")
#q2

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if marks <= 100 and marks >= 0:
            self.__marks = marks
            print("marks stored",marks)


        else:
            print("marks not stored")

    def get_marks(self):
        return self.__marks

mark = Student(100)

mark.set_marks(85)
print(mark.get_marks())
print("---------------------------")

#q3
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print("Salary increased by", amount)
        else:
            print("Invalid increment amount")

    def get_salary(self):
        return self.__salary


sal1 = Employee(100000)

sal1.increase_salary(5000)
print("Current Salary:", sal1.get_salary())

print("---------------------------")
#Level 2
#q4
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money added:", amount)
        else:
            print("Invalid amount")

    def spend_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Money spent:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        return self.__balance


# Testing
wallet = Wallet(1000)

wallet.add_money(500)
wallet.spend_money(300)
print("Current Balance:", wallet.check_balance())

print("-------------------------")
#q5
class Account:
    def __init__(self, balance, password):
        self.__balance = balance
        self.__password = password

    def withdraw(self, amount, password):
        if password == self.__password:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful:", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid password")

    def check_balance(self):
        return self.__balance


# Testing
acc = Account(100000, "arjun")

acc.withdraw(2000, "arjun")
print("Current Balance:", acc.check_balance())

#10
print("-------------------------------------")
from abc import ABC, abstractmethod


# Abstract Class
class BankSystem(ABC):

    def __init__(self, balance):
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.__balance

    @abstractmethod
    def bank_name(self):
        pass


# Child Class
class MyBank(BankSystem):

    def bank_name(self):
        print("Welcome to MyBank")


# Testing
account = MyBank(10000)

account.bank_name()
account.deposit(2000)
account.withdraw(5000)
print("Current Balance:", account.check_balance())

#11
print("---------------------------")
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"UPI Payment of ₹{amount} successful via UPI ID.")

    def refund(self, amount):
        print(f"UPI Refund of ₹{amount} initiated to UPI ID.")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Credit Card charged ₹{amount}.")

    def refund(self, amount):
        print(f"Refund of ₹{amount} credited to Credit Card.")


class NetBanking(Payment):

    def pay(self, amount):
        print(f"NetBanking transfer of ₹{amount} completed.")

    def refund(self, amount):
        print(f"₹{amount} refunded via NetBanking.")


# Testing
upi = UPI()
card = CreditCard()
net = NetBanking()

upi.pay(1000)
card.pay(2000)
net.pay(3000)

print("------------------")

upi.refund(500)
card.refund(1000)
net.refund(1500)

#12
print("-------------------------------------------")

from abc import ABC, abstractmethod


# Abstract Class
class SmartCar(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def auto_drive(self):
        pass


# Tesla (Electric Car)
class Tesla(SmartCar):

    def __init__(self, battery):
        self.__battery = battery   # Encapsulation

    def start_engine(self):
        if self.__battery > 0:
            print("Tesla started silently 🔋")
        else:
            print("Battery empty. Please charge.")

    def auto_drive(self):
        if self.__battery > 10:
            self.__battery -= 10
            print("Tesla is driving autonomously.")
        else:
            print("Not enough battery for auto drive.")


# BMW (Petrol Car)
class BMW(SmartCar):

    def __init__(self, fuel):
        self.__fuel = fuel   # Encapsulation

    def start_engine(self):
        if self.__fuel > 0:
            print("BMW engine started with roar ⛽")
        else:
            print("Fuel empty. Please refill.")

    def auto_drive(self):
        if self.__fuel > 5:
            self.__fuel -= 5
            print("BMW is driving in auto mode.")
        else:
            print("Not enough fuel for auto drive.")


# Testing
tesla = Tesla(50)
bmw = BMW(30)

tesla.start_engine()
tesla.auto_drive()

print("------------------")

bmw.start_engine()
bmw.auto_drive()