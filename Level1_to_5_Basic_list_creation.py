# 1

list1 = [2,5,7,8,6]
print(list1)

#2

list2 = [2,3,4,"akshay","rushikesh",3.5]
print(list2)

#3
list3 = []
list3.append(3,)
list3.append(5,)
list3.append(7,)
print(list3)

#4 Create a list of 5 fruits and print the third fruit

list4 = ["mango", "banana","apple","chiku"]
print(list4[2])

#5 Print the last element of a list using negative indexing.

list5 =  [2,4,5,78,7]
print(list5[-1])


# level 2
#6
nums = [10, 20, 30, 40, 50, 60]


# Print elements from index 1 to 4.

# Print every second element.

# Reverse the list using slicing.

print(nums[0:5])
print(nums[::2])
print(nums[::-1])

#7 Extract first 3 elements from a list.

print(nums[0:3])

#8 Extract last 2 elements using negative indexing

print(nums[-2:])

#9  Write a program to check whether an element exists in a list.

counts = nums.count(10)
print(counts)


#level 3  List Methods Practice

#10 Add 3 grocery items using append().

grocery = []
grocery.append("mango")
grocery.append("banana")
grocery.append("apple")

print(grocery)

#11 Add multiple items using extend().

grocery.extend(["chiku","coconut","guava","chery"])
print(grocery)

#12   Insert "Oil" at index 2 in a grocery list

grocery.insert(2,"oil")
print(grocery)

#13 Remove a specific item from a list.

grocery.remove("chery")
print(grocery)


#14  Remove last element using pop().

grocery.pop()
print(grocery)

#15  Clear the entire list using clear().


grocery.clear()
print(grocery)

#16 Count how many times 5 appears in: nums = [1, 5, 3, 5, 7, 5]

nums = [1, 5, 3, 5, 7, 5]
print(nums.count(5))

#17   Find index of "Apple" in a fruit list.

fruits = ["apple", "banana", "cherry"]
print(fruits.index("apple"))

#18  Sort a list of numbers.

nums.sort()
print(nums)

#19 Reverse a list using reverse().

nums.reverse()
print(nums)


#Level 4   Logic-Based Questions

#20  Write a program to find the largest element in a list.

list = [1,2,3,4,5,6,7,8,9]
list.sort()
print(list)
print(list[-1])

#21  Write a program to find the smallest element in a list.

list2 = [76,45,56,78,32,77,237,]
list2.sort()
print(list2[0])

#22 Calculate sum of all elements in a list.

list3 = [34,6,78,34,78,23]
print(sum(list3))


#23 Count even and odd numbers in a list

list4 = [43,34,5,3,56,32,34,78]


#24 Remove duplicates from a list.

list5 = [34,56,87,90,78,564,34]


#25  Merge two lists into one.

list6 = [32,56,76,8,74,84]
list7 = [63,5,6,4,74,3]
print(list6 + list7)


# level 5
#26  Create a list of 10 numbers using user input.

user = []
ii = int(input("Enter a number: "))
user.append(ii)
user.append(1)
print(user)

#27  Replace the second element of a list with a new value.

list8 = [23,56,87,3,23,8,3]
list8.remove