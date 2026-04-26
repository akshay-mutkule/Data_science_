import threading
import time
import random
import json
from collections import defaultdict
from functools import wraps

# ==============================
# Utility Decorators
# ==============================

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} sec")
        return result
    return wrapper

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# ==============================
# Data Models using OOP
# ==============================

class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.transactions = []

    def add_transaction(self, txn):
        self.transactions.append(txn)

    def total_spent(self):
        return sum(t.amount for t in self.transactions)

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.age})"


class Transaction:
    def __init__(self, txn_id, amount, category):
        self.txn_id = txn_id
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Txn({self.txn_id}, {self.amount}, {self.category})"


# ==============================
# Data Generator using Generator
# ==============================

def transaction_generator(n):
    categories = ['food', 'travel', 'shopping', 'bills']
    for i in range(n):
        yield Transaction(
            txn_id=i,
            amount=random.randint(10, 500),
            category=random.choice(categories)
        )


# ==============================
# Data Processing
# ==============================

class DataProcessor:

    def __init__(self):
        self.users = {}

    def create_users(self, n):
        for i in range(n):
            self.users[i] = User(i, f"User{i}", random.randint(18, 60))

    def assign_transactions(self, txn_count):
        for txn in transaction_generator(txn_count):
            user = random.choice(list(self.users.values()))
            user.add_transaction(txn)

    def category_summary(self):
        summary = defaultdict(int)
        for user in self.users.values():
            for txn in user.transactions:
                summary[txn.category] += txn.amount
        return summary

    def top_users(self, n=5):
        return sorted(self.users.values(), key=lambda u: u.total_spent(), reverse=True)[:n]


# ==============================
# File Handling
# ==============================

class FileManager:

    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)


# ==============================
# Multithreading Example
# ==============================

class WorkerThread(threading.Thread):

    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"[THREAD START] {self.name}")
        time.sleep(self.delay)
        print(f"[THREAD END] {self.name}")


# ==============================
# Mock API Simulation
# ==============================

class MockAPI:

    @staticmethod
    def fetch_data():
        time.sleep(1)
        return {"status": "success", "data": random.sample(range(100), 10)}

    @staticmethod
    def post_data(data):
        time.sleep(0.5)
        return {"status": "posted", "data": data}


# ==============================
# Advanced Python Features
# ==============================

class AdvancedFeatures:

    @staticmethod
    def list_comprehension_example():
        return [x**2 for x in range(20) if x % 2 == 0]

    @staticmethod
    def lambda_sort_example(data):
        return sorted(data, key=lambda x: x['value'])

    @staticmethod
    def map_filter_example():
        data = list(range(50))
        filtered = filter(lambda x: x % 3 == 0, data)
        mapped = map(lambda x: x * 2, filtered)
        return list(mapped)


# ==============================
# Exception Handling
# ==============================

def risky_function(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Division by zero error"


# ==============================
# Main Execution Logic
# ==============================

@timer
@debug
def main():
    processor = DataProcessor()
    processor.create_users(50)
    processor.assign_transactions(500)

    print("\nTop Users:")
    for user in processor.top_users():
        print(user, user.total_spent())

    print("\nCategory Summary:")
    print(processor.category_summary())

    # File save
    FileManager.save_to_json(
        {u.user_id: u.total_spent() for u in processor.users.values()},
        "users.json"
    )

    # Threads
    threads = []
    for i in range(3):
        t = WorkerThread(f"T{i}", random.randint(1, 3))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # API Simulation
    api_data = MockAPI.fetch_data()
    print("\nAPI Data:", api_data)

    print("Post Response:", MockAPI.post_data(api_data))

    # Advanced features
    print("\nAdvanced Features:")
    print(AdvancedFeatures.list_comprehension_example())
    print(AdvancedFeatures.map_filter_example())

    # Exception
    print("\nException Test:")
    print(risky_function(0))
    print(risky_function(5))


# ==============================
# Extra Practice Functions
# ==============================

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ==============================
# Entry Point
# ==============================

if __name__ == "__main__":
    main()

    print("\nFibonacci:", fibonacci(10))
    arr = [random.randint(1, 100) for _ in range(20)]
    sorted_arr = quick_sort(arr)
    print("\nSorted:", sorted_arr)
    print("Search 50:", binary_search(sorted_arr, 50))