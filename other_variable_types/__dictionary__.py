# Dictionary is a collection of data that store data value in key
# A dictionary is ordered, changeable and don't allow duplicates.
# The access of the elements are make with key - value
# 

d = {} # d is an empty dictionary
print("The type of the d variabile is", type(d)) # the function type help us to identify the type of the variable

#other way to create an empty dictionary
d_1 = dict()
print("The type of the d variabile is", type(d_1)) 

my_dict = {"Vlad": 30, "Andreea": 28, "Marius": 25, "Gabi": 45}
print("my_dict:", my_dict)

#other way to create a dictionary
my_dict = dict([('Vlad', 29), ('Andreea', 30), ('Marius', 28), ('Gabi', 50)])
print("my_dict:", my_dict)

# to find the number of element of a dict you need to use "len"
print("length of the dict is:", len(my_dict))

# other way to find the length is with function "__len__()"
print("length of the dict is:", my_dict.__len__())

# if you want to access an element you need to use the key of element
print("what age do Vlad have?", my_dict["Vlad"])

# if you use a key there isn't in dictionary python throw an error: KeyError
try:
    print("What age do Gabriela have?", my_dict["Gabriela"])
except KeyError:
    print("There isn't the key!")

# other metode to access the element is to use the function "get"
print("Andreea age is:", my_dict.get("Andreea"))

# if there isn't the key, function "get" will return "None".
# This is a difference when access directly the element with the key and when you use function "get"
print("Gabriela age is:", my_dict.get("Gabriela"))

# function get offer the possibility if don't find the value of the key that you insert, to return a default value
print("Gabriela age is:", my_dict.get("Gabriela", "Not in the dictionary"))

# if you want to verify if a key exist in the dictionary you can use "in" operator
print("Is Gabriela in dictionary?", 'Gabriela' in my_dict)

# if you want to verify if a key doesn't exist in the dictionary you can use "not in" operator
print("Isn't Gabriela in dictionary?", 'Gabriela' not in my_dict)

# Update a dictionary
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
print("stocks list:", stocks)

# if you want to update a absolut value with the help of a key
stocks['GOOG'] = 900 
print("stocks list:", stocks)

# if you want to remove an element from dictionary you can use "del" function
del(stocks["IBM"])
print("stocks list:", stocks)

# if you want to add a new element and also to update the existing once
stocks.update({'IBM': 200, "AAPL": 500})
print("stocks list:", stocks)

# other way to insert a new element in a dictionary
stocks["TSLA"] = 500
print("stocks list:", stocks)

# if you want to remove an element from dictionary and also to return the value of it
# you can use function "pop"
removed_element = stocks.pop("AAPL")
print("stocks list:", stocks)
print("value of remove element is:", removed_element)

# also if you want to return a defauld value if the key is not found 
# you can use function "pop"

removed_element = stocks.pop("AAPL", -1)
print("stocks list:", stocks)
print("value of remove element is:", removed_element)

# if you want to cross a dictionary you can do by:
# 1. key
for val in stocks.keys():
    print(val)

# 2. value
for val in stocks.values():
    print(val)

# 3. item
for val in stocks.items():
    print(val)
