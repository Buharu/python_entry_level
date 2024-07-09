# a tuple is a collection of data, as a list from other language, but the difference is that are unchangeable
# unchangeable - we can't change an element. The error that will be rise is IndexError

tuple_1 = () # construction of an empty tuple
tuple_1 = tuple() # it has the same effect like "tuple_1 = ()", initialize an empty tuple
tuple_1 = (1) # in this situation Python language will see it like an int
print(type(tuple_1)) # <class 'int'>
tuple_1 = (1,) # because we added that comma at the end will become a tuple
print(type(tuple_1)) # <class 'tuple'>

tuple_2 = (1, 2, "New Element", True)
print(len(tuple_2)) # the function "len" will return the tuple length
print(tuple_2.__len__()) # the second way to find the tuple length

# how to access an element from a tuple
print(tuple_2[0]) # first element
print(tuple_2[3]) # the last element, the 4'th elment
try:
    print(tuple_2[4])
    # The error will be if you try to run out of block "try"
#       Traceback (most recent call last):
#          File "<stdin>", line 1, in <module>
#       IndexError: tuple index out of range
except:
    print("The index is out of range. the interval of values are: (", len(tuple_2) - 1,", " ,(-1) * (len(tuple_2) - 1), ")") 

print(tuple_2[-1]) # the tuple work like a string, it will return "True", the last element
print(tuple_2[1:3]) # will return the value from index 1 to 2, without 3

tuple_2 = tuple_2 + ("four index", "element six", False) # we can't add or concatenate 2 tuple, we only can build a new one
print("the new tuple:", tuple_2)

tuple_3 = tuple_2 * 2 # the operator "*" will multiply the current tuple
print("tuple_3:", tuple_3)

tuple_4 = (1, 7, 5, 3, 5, 6)
print(max(tuple_4)) # if the tuple has only value, without any string, will return the max value
print(min(tuple_4)) # the min value

# if you want to cross a tuple you can use for
for i in tuple_4:
    print(i)

# any change to a tuple will generate an error
try:
    tuple_4[0] = 2 # change "1" with "2"
except TypeError:
    print("ERROR: you try to change an element")

try:
    tuple_4.__reversed__()
except AttributeError:
    print("ERROR: 'tuple' object has no attribute '__reversed__'")

try:
    tuple_4.sort()
except AttributeError:
    print("ERROR: 'tuple' object has no attribute 'sort'")
    
try:
    del(tuple_4[1])
except TypeError:
    print("ERROR: 'tuple' object doesn't support item deletion")

