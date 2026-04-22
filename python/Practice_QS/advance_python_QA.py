"""
ADVANCED PYTHON PRACTICE PROJECT
Banking & Transaction Processing System
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Generator
import threading
import multiprocessing
import asyncio
import time
import logging
from contextlib import contextmanager
from functools import wraps

# ----------------------- LOGGING SETUP -----------------------

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------- CUSTOM EXCEPTIONS -----------------------

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


# ----------------------- DECORATORS -----------------------

def transaction_logger(func):
    """Function decorator for logging transactions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completed {func.__name__}")
        return result
    return wrapper


def execution_timer(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


# ----------------------- ABSTRACT CLASS -----------------------

class Account(ABC):

    def __init__(self, account_number: int, holder_name: str, balance: float):
        self._account_number = account_number   # Encapsulation
        self._holder_name = holder_name
        self._balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    @property
    def balance(self):
        return self._balance

    @transaction_logger
    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    @transaction_logger
    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self._balance:
            raise InsufficientBalanceError("Not enough balance")
        self._balance -= amount
        print(f"Withdrew {amount}. New Balance: {self._balance}")


# ----------------------- INHERITANCE -----------------------

class SavingsAccount(Account):

    def calculate_interest(self):
        interest = self._balance * 0.04
        self._balance += interest
        print(f"Interest Added: {interest}")


class CurrentAccount(Account):

    def calculate_interest(self):
        print("No interest for Current Account")


# ----------------------- DATACLASS -----------------------

@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float


# ----------------------- GENERATOR -----------------------

def transaction_generator(transactions: List[Transaction]) -> Generator:
    for txn in transactions:
        yield f"{txn.sender} -> {txn.receiver} : {txn.amount}"


# ----------------------- CONTEXT MANAGER -----------------------

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


# ----------------------- ITERATOR -----------------------

class Fibonacci:

    def __init__(self, max_count):
        self.max_count = max_count
        self.n1, self.n2 = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        value = self.n1
        self.n1, self.n2 = self.n2, self.n1 + self.n2
        self.count += 1
        return value


# ----------------------- MULTITHREADING -----------------------

def process_transaction(name):
    print(f"Processing transaction for {name}")
    time.sleep(2)
    print(f"Completed transaction for {name}")


# ----------------------- MULTIPROCESSING -----------------------

def heavy_computation(n):
    total = sum(i * i for i in range(n))
    print(f"Computed sum of squares up to {n}")
    return total


# ----------------------- ASYNC PROGRAMMING -----------------------

async def async_task(name):
    print(f"Async task started: {name}")
    await asyncio.sleep(2)
    print(f"Async task completed: {name}")


# ----------------------- MAIN EXECUTION -----------------------

@execution_timer
def main():

    # Create accounts
    acc1 = SavingsAccount(101, "Munna", 10000)
    acc2 = CurrentAccount(102, "Ravi", 5000)

    # Perform transactions
    acc1.deposit(2000)
    acc1.withdraw(1500)
    acc1.calculate_interest()

    # Dataclass usage
    transactions = [
        Transaction("Munna", "Ravi", 500),
        Transaction("Ravi", "Amit", 300)
    ]

    # Generator usage
    print("\nGenerated Transactions:")
    for txn in transaction_generator(transactions):
        print(txn)

    # List comprehension
    squares = [x*x for x in range(10)]
    print("\nSquares:", squares)

    # Lambda & map
    doubled = list(map(lambda x: x*2, squares))
    print("Doubled:", doubled)

    # Custom Iterator
    print("\nFibonacci Series:")
    for num in Fibonacci(10):
        print(num, end=" ")

    # File Handling with Context Manager
    with file_manager("transactions.txt", "w") as f:
        for txn in transactions:
            f.write(f"{txn}\n")

    # Multithreading
    print("\n\nStarting Threads...")
    t1 = threading.Thread(target=process_transaction, args=("Munna",))
    t2 = threading.Thread(target=process_transaction, args=("Ravi",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Multiprocessing
    print("\nStarting Multiprocessing...")
    p1 = multiprocessing.Process(target=heavy_computation, args=(1000000,))
    p1.start()
    p1.join()

    # Async execution
    print("\nStarting Async Tasks...")
    asyncio.run(asyncio.gather(
        async_task("Task1"),
        async_task("Task2")
    ))


if __name__ == "__main__":
    main()