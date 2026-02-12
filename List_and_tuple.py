#  List

list =[10,20,"akshay","rushi"]
print(list)
print(list[3])
list2 = ["aggs","milks","bread","apple","banana"]
print(list2)

# indexing
# we are print element individualy in

print(list2[0])
print(list2[3])
print(list2[-1])


#slicing

list3 = ["aggs","milks","bread","apple","banana"]
print(list3[0:3])
print(list3[0:])
print(list3[0:3:2])   # 

# list function/methods


grocery = ["aggs","milks","bread","apple","banana" ]
# append()
# add single element at last

grocery.append("Butter")
print(grocery)

# extend
#Add multiple element at the last

grocery.extend(["sugar","salt","lemon"])
print(grocery)


#insert()
# add element at speecific index

grocery.insert(1,"poha")
print(grocery)

#Remove
# Remove element based on value

grocery.remove("poha")
print(grocery)

#pop()
# pop remove element on index if you not give index it remove last index
grocery.pop(3)
print(grocery)

#clear
# clear remove all element

grocery.clear()
print(grocery)






numbers = [2,1,2,3,4,1,3,5,4,4]


#index()
# to find index of the element


print(numbers.index(4))

# count()
#number of element
print(numbers.count(1))

#sort()
#sort element in assending order

numbers.sort()
print(numbers)

#reverse
#reverse a string

numbers.reverse()
print(numbers)





