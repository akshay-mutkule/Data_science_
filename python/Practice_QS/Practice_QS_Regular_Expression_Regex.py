<<<<<<< HEAD

import re

#PART 1: Basic Pattern Matching
#1 Find the Word
# Text:
# text = "The cat is sleeping. The dog is barking.
# 👉 Extract the word "cat"


text = "The cat is sleeping. The dog is barking."
pattern = re.search("cat", text)
print(pattern.group())

#2 Find All Digit
# Text:
# text = "My marks are 85, 90 and 78."
# 👉 Extract all numbers.

text = "My marks are 85, 90 and 78."
pattern = re.findall(r"[0-9]\d", text)
print(pattern)

#3Find Words Starting with 'c'
# Text:
# text = "cat car dog cow cup bat"
# 👉 Extract words starting with letter c

text = "cat car dog cow cup bat"
pattern = re.findall(r"\bc\w*", text)
print(pattern)

#4  Find 4-Letter Words
# Text:
# text = "This book is very good and easy
# 👉 Extract all 4-letter words

text = "This book is very good and easy"
pattern = re.findall(r"\w\w\w\w", text)
print(pattern)

#PART 2: Using search() and match()

#5 Check If String Starts with Number
# Text:
# text = "9876543210 is my number"
# 👉 Use match() to check if it starts with 10 digits.

text = "9876543210 is my number"
pattern = re.match(r"\d{10}",text)
print(pattern.group())


#6Find First Email

# Text:
# text = "Contact at help@gmail.com or info@yahoo.com"
# 👉 Use search() to extract the first email


text = "Contact at help@gmail.com or info@yahoo.com"
pettern = re.search(r"\w+@\w+\.\w+",text)
print(pettern.group())

#PART 3: Using findall()
#7
# Extract All Phone Numbers
# Text:
# text = "Call me at 9876543210 or 9123456789"
# 👉 Extract all 10-digit numbers.

text = "Call me at 9876543210 or 9123456789"
pattern = re.findall(r"\d+",text)
print(pattern)

#8 Extract All Dates
# Text:
# text = "Meeting on 12-03-2026 and 15-04-2026"
# 👉 Extract all dates.
text = "Meeting on 12-03-2026 and 15-04-2026"
pattern = re.findall(r"\d{2}-\d{2}-\d{4}",text)
print(pattern)

#PART 4: Using sub()
#9 Replace cat with dog
# Text:
# text = "The cat is here."
# 👉 Replace "cat" with "dog".
text = "The cat is here."
pattern = re.sub("cat","Dog",text)
print(pattern)

#10 Hide Phone Numbers
# Text:
# text = "My number is 9876543210"
# 👉 Replace digits with *
# Expected Output:
# My number is ****

text = "My number is 9876543210"
pattern =re.sub("[0-9]","*",text)
print(pattern)

#PART 5: Using split()
#11 Split by Comma
# Text:
# text = "apple,banana,mango,grapes"
# 👉 Split into list.

text = "apple,banana,mango,grapes"
pattern = re.split(r"[,]",text)
print(pattern)

#12 Split by Space or Comma
# Text:
# text = "apple, banana mango"
# 👉 Split properly.
text = "apple, banana mango"
pattern  = re.split(r"[,\s]",text)
print(pattern)

#PART 6: Practical Real-Life Questions
# #13  Extract Email from Resume
# Text:
# text = "Name: Rahul\nEmail: rahul123@gmail.com\nPhone: 9876543210"
# 👉 Extract email only.

text = "Name: Rahul\nEmail: rahul123@gmail.com\nPhone: 9876543210"
pattern = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
print(pattern.group())

#14 Extract Indian Mobile Number
# Text:
# text = "Contact: +919876543210"
# 👉 Extract valid Indian mobile number.

text = "Contact: +919876543210"
pattern = re.findall(r"(?:\+91{\s-}?|0)?[6-9]\d{9}",text)
print(pattern)
print(pattern)

=======

import re

#PART 1: Basic Pattern Matching
#1 Find the Word
# Text:
# text = "The cat is sleeping. The dog is barking.
# 👉 Extract the word "cat"


text = "The cat is sleeping. The dog is barking."
pattern = re.search("cat", text)
print(pattern.group())

#2 Find All Digit
# Text:
# text = "My marks are 85, 90 and 78."
# 👉 Extract all numbers.

text = "My marks are 85, 90 and 78."
pattern = re.findall(r"[0-9]\d", text)
print(pattern)

#3Find Words Starting with 'c'
# Text:
# text = "cat car dog cow cup bat"
# 👉 Extract words starting with letter c

text = "cat car dog cow cup bat"
pattern = re.findall(r"\bc\w*", text)
print(pattern)

#4  Find 4-Letter Words
# Text:
# text = "This book is very good and easy
# 👉 Extract all 4-letter words

text = "This book is very good and easy"
pattern = re.findall(r"\w\w\w\w", text)
print(pattern)

#PART 2: Using search() and match()

#5 Check If String Starts with Number
# Text:
# text = "9876543210 is my number"
# 👉 Use match() to check if it starts with 10 digits.

text = "9876543210 is my number"
pattern = re.match(r"\d{10}",text)
print(pattern.group())


#6Find First Email

# Text:
# text = "Contact at help@gmail.com or info@yahoo.com"
# 👉 Use search() to extract the first email


text = "Contact at help@gmail.com or info@yahoo.com"
pettern = re.search(r"\w+@\w+\.\w+",text)
print(pettern.group())

#PART 3: Using findall()
#7
# Extract All Phone Numbers
# Text:
# text = "Call me at 9876543210 or 9123456789"
# 👉 Extract all 10-digit numbers.

text = "Call me at 9876543210 or 9123456789"
pattern = re.findall(r"\d+",text)
print(pattern)

#8 Extract All Dates
# Text:
# text = "Meeting on 12-03-2026 and 15-04-2026"
# 👉 Extract all dates.
text = "Meeting on 12-03-2026 and 15-04-2026"
pattern = re.findall(r"\d{2}-\d{2}-\d{4}",text)
print(pattern)

#PART 4: Using sub()
#9 Replace cat with dog
# Text:
# text = "The cat is here."
# 👉 Replace "cat" with "dog".
text = "The cat is here."
pattern = re.sub("cat","Dog",text)
print(pattern)

#10 Hide Phone Numbers
# Text:
# text = "My number is 9876543210"
# 👉 Replace digits with *
# Expected Output:
# My number is ****

text = "My number is 9876543210"
pattern =re.sub("[0-9]","*",text)
print(pattern)

#PART 5: Using split()
#11 Split by Comma
# Text:
# text = "apple,banana,mango,grapes"
# 👉 Split into list.

text = "apple,banana,mango,grapes"
pattern = re.split(r"[,]",text)
print(pattern)

#12 Split by Space or Comma
# Text:
# text = "apple, banana mango"
# 👉 Split properly.
text = "apple, banana mango"
pattern  = re.split(r"[,\s]",text)
print(pattern)

#PART 6: Practical Real-Life Questions
# #13  Extract Email from Resume
# Text:
# text = "Name: Rahul\nEmail: rahul123@gmail.com\nPhone: 9876543210"
# 👉 Extract email only.

text = "Name: Rahul\nEmail: rahul123@gmail.com\nPhone: 9876543210"
pattern = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
print(pattern.group())

#14 Extract Indian Mobile Number
# Text:
# text = "Contact: +919876543210"
# 👉 Extract valid Indian mobile number.

text = "Contact: +919876543210"
pattern = re.findall(r"(?:\+91{\s-}?|0)?[6-9]\d{9}",text)
print(pattern)
print(pattern)

>>>>>>> 276650d (files)
