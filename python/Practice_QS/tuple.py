<<<<<<< HEAD
 #Tuple

tup = (1,2,3,"rushi","Akshay")
print(tup)

# if you want to print size of memory alocation

import sys
list1 = [1,2,3]
tup1 = (1,2,3)

print(sys.getsizeof(list1))
print(sys.getsizeof(tup1))

# in tuple only two functions are used
tup2 = (1,3,5,6,7,7,4,85,8,4)
print(tup2.count(1))
print(tup2.index(4))


tup3 = (1,3,5,6,7,7,4,85,8,4)

print(tup3[3])
print(tup3[4])
print(tup3[-1])
print(tup3[-2])


print(tup3[0:4])
print(tup3[5:])
print(tup3[::-1])
print(tup3[::2])

new_tup = tup3[1:6]
print(new_tup)

tup4 = (1,3,5,6,7,7,4,85,8,4)
tup5 = (95,67,7,4,85,8,4)
new_tup1 = tup4 + tup5  #Tuple concatination
print(new_tup1)

 



=======
 #Tuple

tup = (1,2,3,"rushi","Akshay")
print(tup)

# if you want to print size of memory alocation

import sys
list1 = [1,2,3]
tup1 = (1,2,3)

print(sys.getsizeof(list1))
print(sys.getsizeof(tup1))

# in tuple only two functions are used
tup2 = (1,3,5,6,7,7,4,85,8,4)
print(tup2.count(1))
print(tup2.index(4))


tup3 = (1,3,5,6,7,7,4,85,8,4)

print(tup3[3])
print(tup3[4])
print(tup3[-1])
print(tup3[-2])


print(tup3[0:4])
print(tup3[5:])
print(tup3[::-1])
print(tup3[::2])

new_tup = tup3[1:6]
print(new_tup)

tup4 = (1,3,5,6,7,7,4,85,8,4)
tup5 = (95,67,7,4,85,8,4)
new_tup1 = tup4 + tup5  #Tuple concatination
print(new_tup1)

 



>>>>>>> 276650d (files)
