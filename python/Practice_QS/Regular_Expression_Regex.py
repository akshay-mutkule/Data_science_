<<<<<<< HEAD
# Symbol
# Meaning
# Example
# .Any
# character except newline
# a.c → abc, aac
# \d
# Any
# digit(0–9)    \d → 5
# \Dvqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqt
# Not
# a
# digit    \D → a
# \w
# Word
# character(a - z, A - Z, 0 - 9, _)    \w → a, 5
# \W
# Not
# a
# word
# character    \W →
#
# @
#
# \s
# Whitespace(space, tab)    \s
# \S
# Not
# whitespace    \S
#
# Symbol
# Meaning
# Example
# *0 or more
# times
# a * → "", a, aa
# +    1 or more
# times
# a + → a, aa
# ?    0 or 1
# time(optional)
# a? → "", a
# {n}
# Exactly
# n
# times    \d
# {3}
# {n, }
# At
# least
# n
# times    \d
# {2, }
# {n, m}
# Between
# n and m
# times    \d
# {2, 4}
#Pattern Meaning
# \d

import re
# findall - find all maching text
text = "call me at +91-9876543210,0987654321"
pattern = r"(?:\+91{\s-}?|0)?[6-9]\d{9}"
numbers = re.findall(pattern, text)
print(numbers)

# Search = find the first maching text

text = "call me at +91-9876543210,0987654321"
pattern =  r"(?:\+91{\s-}?|0)?[6-9]\d{9}"
numbers = re.search(pattern, text)
print(numbers.group())



text = "The cat is sitting, the cat is very cute"

result = re.search("cat", text)
print(result.group())


text = "cat is sitting, the cat is very cute"
result = re.match("cat", text)
print(result.group())


text = " apple mango banana orange"
result = re.split(r"[,: ]", text)
print(result)

text = "The cat is sleeping"
result = re.sub(pattern, "dog", text)
print(result)

text = "Email: test@gmail.com"
pattern = r"\w+@\w+\.\w+"
print(re.findall(pattern, text))


=======
# Symbol
# Meaning
# Example
# .Any
# character except newline
# a.c → abc, aac
# \d
# Any
# digit(0–9)    \d → 5
# \Dvqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqt
# Not
# a
# digit    \D → a
# \w
# Word
# character(a - z, A - Z, 0 - 9, _)    \w → a, 5
# \W
# Not
# a
# word
# character    \W →
#
# @
#
# \s
# Whitespace(space, tab)    \s
# \S
# Not
# whitespace    \S
#
# Symbol
# Meaning
# Example
# *0 or more
# times
# a * → "", a, aa
# +    1 or more
# times
# a + → a, aa
# ?    0 or 1
# time(optional)
# a? → "", a
# {n}
# Exactly
# n
# times    \d
# {3}
# {n, }
# At
# least
# n
# times    \d
# {2, }
# {n, m}
# Between
# n and m
# times    \d
# {2, 4}
#Pattern Meaning
# \d

import re
# findall - find all maching text
text = "call me at +91-9876543210,0987654321"
pattern = r"(?:\+91{\s-}?|0)?[6-9]\d{9}"
numbers = re.findall(pattern, text)
print(numbers)

# Search = find the first maching text

text = "call me at +91-9876543210,0987654321"
pattern =  r"(?:\+91{\s-}?|0)?[6-9]\d{9}"
numbers = re.search(pattern, text)
print(numbers.group())



text = "The cat is sitting, the cat is very cute"

result = re.search("cat", text)
print(result.group())


text = "cat is sitting, the cat is very cute"
result = re.match("cat", text)
print(result.group())


text = " apple mango banana orange"
result = re.split(r"[,: ]", text)
print(result)

text = "The cat is sleeping"
result = re.sub(pattern, "dog", text)
print(result)

text = "Email: test@gmail.com"
pattern = r"\w+@\w+\.\w+"
print(re.findall(pattern, text))


>>>>>>> 276650d (files)
