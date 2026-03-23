# # Basic Tuple creation
#
# #1 Create a tuple containing 5 integers and print it.
# tup = (1,2,3,4,5)
# print(tup)
#
#
# #2   Create a tuple containing mixed data types (int, float, string).
# tup1 = (1,2,3,"Akshay",2.77,"saurabh")
# print(tup1)
#
#
#
# #3 Create a single-element tuple correctly.
# tup2 = (1,)
# print(tup2)
#
#
#
# #4  Check the datatype of:  t = (5) Why is it not a tuple?
# tup3 = (2)
# print(type(tup3))  # if in round bracket there is a sigle value it take as a integer or str
# tup3 = ("Akshay")
# print(type(tup3))
#
#
# #5 Create a tuple without using parentheses.
# t = 1,2,3,3,4,5
# print(type(t))
#
#
# #Level2
# # indexing and slicing
#
# #6Given:
#
from multiprocessing.reduction import duplicate

nums = [10, 20, 30, 40, 50, 60]

# # Print first element
print(nums[0])
#print the last element using negative indexing
print(nums[-1])
# Extract elements from index 1 to 4.
nums.pop(1)
nums.pop(1)
nums.pop(1)
nums.pop(1)
print(nums)
# # Print every second element.
print(nums[::2])
# # Reverse the list using slicing.
print(nums[::-1])

#7 Extract first 3 elements from a list

nums1 = [23,3,5,3,4,23,5]
nums1.remove(23)
nums1.remove(5)
nums1.remove(3)
print(nums1)

#8  Extract last 2 elements using negative indexing

nums2 = [3,5,7,7,5476,43,6743,6743]
print(nums2[0:-2])


#9  Extract last 3 elements using slicing.

t = (10, 20, 30, 40, 50, 60)
print(t[0:3])

#10 Reverse the tuple using slicing.
print(t[::-1])

#11 Get every second element using slicing.

print(t[::2])

# Level 3
# Tuple Methods

#Given:

t = (1, 2, 3, 2, 4, 2)

#12 Count how many times 2 appears.
print(t.count(2))


#13 Find the index of element 4
print(t.index(4))

#14 What happens if you search for an element that does not exist?
print(t.count(34))  # it gives 0



# Level 4
# logic-based question


#15 Write a program to find the maximum value in a tuple.

tup = (12,43,65,4356,43,634,67)
largest = max(tup)
print(largest)

#16  Write a program to find the minimum value in a tuple.
minimum = min(tup)
print(minimum)

#17 Calculate the sum of elements in a tuple
addition = sum(tup)
print(addition)

#18 Check whether a value exists in a tuple.
if 43 in tup:
    print("exist")
else:
    print("not exist")

#19 Convert a tuple into a list.
lists = list(tup)
print(lists)

#20 Convert a list into a tuple.
tuup = tuple(lists)
print(tuup)

# Level 5
#Nested Tuple
#Given:

t1 = ((1, 2), (3, 4), (5, 6))

#21  Access element 4.
print(t1[1][1])

#22 Access element 6.
print(t1[2][1])

#23 Extract the second inner tuple.
print(t1[::2])

#24 Find the sum of all elements in nested tuple.
total = sum(sum(inner) for inner in t1)
print(total)

# LEVEL 6: Advanced Practice


#25 Create a tuple of student names and print them in sorted order.

student = ("akshay", "olm","sham","esaumya")
sort = sorted(student)
print(sort)

#26 Create a tuple and check if it is a palindrome.
tup11 = (1,2,1)
if tup11 ==tup11[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")

#27 Swap two tuples.

t11 = [21,32,4,2,4]
t22 = [23,67,7,548,86]
t11,t22 = t22,t11
print(t11)
print(t22)

#28 Unpack a tuple into three variables. Example:

t = (10, 20, 30)
a,b,c = t
print(a)
print(b)
print(c)


#29 What happens if you unpack more values than variables?
tup3 = (2,34,2,4)
a,b,c,d = tup3

print(a)
print(b)
print(c)
print(d)
# it shows error  not enough values to unpack

#Level 7  Practical Mini Tasks


# 30 Store latitude and longitude in a tuple and print them.
tup4 = (18.5204, 73.8567)
print("location :",tup4)
print("longitude:",tup4[0])
print("latitude:",tup4[1])

#31 Create a tuple of 5 numbers and calculate their average.
tup5 = (2,43,23,45,23)
sumt = sum(tup5)
print("Average:",(sumt/5))

#32 Store 3 employee records in nested tuple format.

tup6 = (("Akshay",34),("yash",54),("vaibhav",33))
print(tup6)

#33 Extract all second elements from:

tup7 = ((1,10),(2,20),(3,30))
result = tuple(item[1] for item in tup7)
print(result)

#34 Remove duplicates from a tuple.
tup8 = (2,3,2,3,245,3,3,2)
result = tuple(set(tup8))
print(result)

#35  Create a tuple of even numbers from 1 to 20.

even_numbers = tuple(num for num in range(1, 21) if num % 2 == 0)

print(even_numbers)

#  LEVEL 8: Interview Questions


#36Why are tuples immutable?
# for safety and faster than list

#37  Why can tuples be used as dictionary keys but lists cannot?
#Tuples can be used as dictionary keys because they are immutable and hashable, whereas lists are mutable and therefore not hashable.

#38 Which is faster: tuple or list? Why?
# tuple is faster than list because it is immutabal

#39  Can a tuple contain a list inside it?
#yes

#40 Can elements inside a nested list in a tuple be modified?
#yes