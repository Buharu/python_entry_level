# a set variable is a collection of data, that are unordered, unchangeable and unindexed
# unordered - that means after every run, the result will be random
# unchangeable - we can't change an element. The error that will be rise is TypeError
# unindexed - we can't access the element with the help of the index. The error that will be rise is KeyError  

my_set = set() # initilize an empty set
my_set = {0, 1, 2, 3, 4, 5} # when you want to build a set you must build with 

# if you want to create a set from a list you can do it:
my_set_from_list = set([1, 2, 3, 4, 5, 5]) # if you have duplicates, we python create set will remove them
print("The set created from list:", my_set_from_list)

# if you want to initilize an empty set like this:
my_set_2 = {} 
# you will create a dictionary
print(type(my_set_2))

my_new_set = {1, 2, 5, 8, 9}

print(len(my_new_set)) # to findout the length of the set: 5

# the element of a set can't be access by index 
try:
    print(my_new_set[1])
except TypeError: 
    "You can't access an element by index"

# if you want to access the elements of a set you can use "For" statment:
for val in my_new_set:
    print(val)

# aggregation operations
print("The max value from the set is:", max(my_new_set))

print("The min value from the set is:", min(my_new_set))

is_1_in_my_new_set = 1 in my_new_set # return a boolean value
is_6_in_my_new_set = 6 in my_new_set # return a boolean value
print("The value 1 is in set?", is_1_in_my_new_set, ", but 6?", is_6_in_my_new_set)

is_1_in_my_new_set = 1 not in my_new_set # return a boolean value

print("The value 1 isn't in set?", is_1_in_my_new_set, ", but 6?", is_6_in_my_new_set)

# Update operations:
my_set_3 = {1, 2, 3}
print("my_set_3:", my_set_3)

my_set_3.add(4) # if you want to add an element you will use the function "add"
print("my_set_3:", my_set_3)
my_set_3.add(1) # if the element already exist, it would not add to set
print("my_set_3:", my_set_3)

my_set_3.update([4, 5, 6]) #the duplicates will be ignore
print("my_set_3:", my_set_3)

my_set_3.remove(1) # will remove the element that have value equal with "1"
print("my_set_3:", my_set_3)

try:
    my_set_3.remove(1) # if you try to remove a value that don't exist will give you an error
except KeyError:
    print("The element don't exist in set")

print("my_set_3:", my_set_3)
my_set_3.discard(3) # function discard will remove the element with value "3"
print("my_set_3:", my_set_3)

my_set_3.discard(3) # if the element that you want to remove it's in set, the function will not rise an error
print("my_set_3:", my_set_3)

my_set_3.pop() # function "pop" will remove the first element and will return the first element that will have the set
print("my_set_3:", my_set_3)

# Crowd Operations
crowd_a = {1, 2, 3, 4, 5}
print("\ncrowd_a:", crowd_a)
crowd_b = {4, 5, 6, 7, 8}
print("crowd_b:", crowd_b)
crowd_union = crowd_a.union(crowd_b) # will return the values that are in A and B without duplicates if exists
print("crowd_union:", crowd_union)

crowd_intersetion = crowd_a.intersection(crowd_b) # will return the commun values of A and B
print("crowd_intersetion:", crowd_intersetion)

crowd_difference = crowd_a.difference(crowd_b) # will return the values that are present only in A
print("crowd_difference:", crowd_difference)


# Which is the sum of the unique value from the next set?
new_set = set([5, 6, 3, 5, 6, 10, 2, 7, 7, 4, 2, 10, 10, 1, 9, 10, 5, 2, 2, 8, 10, 6, 5, 1, 7, 6, 7, 3, 3, 2, 7, 5, 10, 6, 3, 5, 10, 1, 4, 3, 4, 1, 1, 1, 9, 9, 3, 7, 8, 9, 9, 5, 10, 7, 6, 1, 10, 3, 4, 4, 9, 9, 3, 6, 9, 7, 7, 7, 1, 4, 2, 2, 1, 7, 2, 7, 9, 4, 6, 7, 4, 9, 4, 3, 2, 4, 10, 6, 10, 9, 9, 9, 9, 3, 10, 1, 10, 1, 5, 9])
sum = 0
for i in new_set:
    sum += i
print("sum =", sum)

# How can you union 2 set?
a = {5, 6, 7}
b = {7, 8, 9, 10}
print(a.union(b)) 

# How can you make intersection of a and b?
print(a.intersection(b))

# Which is the result of difference of a with b?
print(a.difference(b))

# remove the element '4' from my_set
my_set ={23, 15, 2.3, '4'}
my_set.remove('4')
print(my_set) #{23, 15, 2.3}

# Do you can insert the element 33 in set_1 on index 2?
set_1 = {45, 77, 23}
try:
    set_1[2] = 33
except TypeError:
    print("An element from a set can't be update because set is unchangeable")
    print("The error that was rise is TypeError")