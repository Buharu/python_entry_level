# Every program works with data, but for used them we need to store in the memory. To store in the memory we need
# first to reserve a memory area
# The best practice for naming a variable are:
#   1. used only letters, numbers and underscore character
#   2. first character must be underscored or letter
#   3. if we want to use a constant variable we need to write it with CAPSLOCK

# Types of variable:
print("Integer values or int values\n")
#   1. Integer or int
var = 10  # var is the name of the variable, "=" is the operator that assign the value to the variable, 10 is the
# value of var

# Operators and operations with INTEGER values
amount = var + 10  # 10 + 10 = 20

# to display the value of the variable sum we use the "print" function
# to concatenate text with a variable you can use comma between them or
print("amount =", amount)  # sum = var + 10, sum = 10 + 10, sum = 20
# you can change the type of the "sum" variable from INTEGER to STRING with function "str" and the concatenation
# can be done with operator "+"
print("amount = " + str(amount))

dif = var - 5  # 10 - 5 = 5
print("dif =", dif)

multiplication = var * 3  # 10 * 3 = 30
print("multiplication =", multiplication)

division = var / 2  # 10 / 2 = 5
print("division = ", division)

exponentiation = var ** 2  # 10 ** 2 = 100
print("exponentiation =", exponentiation)

modulus = var % 3  # 10 % 3 = 1 because 3 * 3 = 9 and the rest is 1
print("modulus =", modulus)

floor_division = var // 7
print("floor_division =", floor_division)  # 10 // 7 = 1 because 7 + 3 = 10 and 7 is only ones.

floor_division = var // 2
print("floor_division =", floor_division)  # 10 // 2 = 5 because 5 * 2 = 10 and 2 is 5 times in 10.

print("\nConversion")
# python language offer us, also, the possibility to convert from a "String" value to "Integer" value
string_10 = "10"
var_10 = int(string_10)
print("var_10 =", var_10)

# In the case the conversion can be use python give us an error:
string_integer_error = "19a"
# to cache an error that blocks your program you can use the block  "try" that gives you the possibility to execute a
# block of code that can rise you an error more about how to handle the error in python on
# https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples

print("\nTry block")
try:
    print(int(string_integer_error))
except:
    print("The number that you tried to convert: \"", string_integer_error, '" is not a number')
    print("ValueError: invalid literal for int() with base 10: '19a'")

print("\nBinary, octa and hexadecimal values:")
# python offer us also the possibility to work with binary, octa or hexa values
# to make the difference between the values we must use:
#       1.1 for binary values "0b" and after that the value
binary_value = 0b0010
# when we print the values binary, octa or hexa value with function "print"
# the interpreter always convert the value in 10 base
print("binary_value = 0b0010 = ", binary_value)

#       1.2 for octa values "0o"
octa_value = 0o0010
print("octa_value = 0o0010 ", octa_value)

#       1.3 for hexa values "0x". in this case to write a number in hexadecimal we can use 0 to 9 and A to F
hexa_value = 0xA1
print("hexa_value = 0xA1 ", hexa_value)

print("\n\nFloat values\n")
#   2. Float
#  it's a type that is used to store the real numbers, with comma
float_value = 10.245
print("float_value =", float_value)

# conversion from "int" to "float"
float_conversion_from_int = float(var)
print("var = ", var, "and float_conversion_from_int = ", float_conversion_from_int)

# conversion from "string" to "float"
float_in_string = "10.245"
float_conversion_from_string = float(float_in_string)
print("float_in_string = ", float_in_string, "and float_conversion_from_string =", float_conversion_from_string)

# in the case of "float" variables we also have:
#   2.1 "nan" = not-a-number
# a good example how to use "nan" value is:
value_from_string_to_float = 0.0
string_float_error = "0.0a"
try:
    value_from_string_to_float = float(string_float_error)
except:
    value_from_string_to_float = float("nan")

print("string_float_error =", string_float_error, " , value_from_string_to_float =",
      value_from_string_to_float, "and type = ", type(value_from_string_to_float))

#   2.2 for float exist also infinite, "inf" and - infinite, "-inf"
infinite = float("inf") + 1000
minus_infinite = float("-inf") + 1000

print("infinite =", infinite, " and minus_infinite =", minus_infinite)

print("\nBoolean\n")
#   3. Boolean

true_value = True
false_value = False

print("true_value = ", true_value, "and false_value =", false_value)

# in python the conversion of can be done also on other type of variables:
value_0 = bool(0)
print("value_0 =", value_0)

value_minus_1 = bool(-1)
print("value_minus_1 =", value_minus_1)

value_float = bool(0.2)
print("value_float =", value_float)

value_empty_lista = bool([])
print("value_empty_lista =", value_empty_lista)

value_lista = bool([1, 2, 3])
print("value_lista [1, 2, 3] =", value_lista)

value_empty_string = bool("")
print("value_empty_string =", value_empty_string)

value_string = bool("Vlad")
print("value_string =", value_string)

value_false_string = bool("False")
print("value_false_string =", value_false_string)

# Build a list that containt all the number from 1 to 99 that are divisible with 2 or 3 or 5. The result that must you obtain:
# Ex: For numbers from 1 to 10, result is [2, 3, 4, 5, 6, 8, 9]

#  first step we create a empty lista
lista = []
count = 0
for i in range(1, 100):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        lista.append(i)
        count += 1

# The result was save on "lista"
print("lista= ", lista, ". Total = ", count)

# How many characters are in the string presented below? (the spaces and punctuation marks are consider characters)
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae consectetur ligula. Ut at est non lacus auctor ornare et non odio. Vestibulum ac neque at velit lacinia consectetur eget non sem. Nam nec ligula ipsum. Donec tincidunt, mi a finibus commodo, ante sem ullamcorper nisl, sed mollis felis purus vel diam. Sed ultricies id metus.

string_on_analysis = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae consectetur ligula. Ut at est non lacus auctor ornare et non odio. Vestibulum ac neque at velit lacinia consectetur eget non sem. Nam nec ligula ipsum. Donec tincidunt, mi a finibus commodo, ante sem ullamcorper nisl, sed mollis felis purus vel diam. Sed ultricies id metus." 
print ("Length = ", len(string_on_analysis))

# Transform all the characters from the string in caps
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dapibus nulla pretium facilisis commodo. Praesent convallis mollis auctor. Maecenas vitae sapien id nunc sodales tincidunt.

string_need_caps = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dapibus nulla pretium facilisis commodo. Praesent convallis mollis auctor. Maecenas vitae sapien id nunc sodales tincidunt."
print ("The new string: ", string_need_caps.upper())

# You have the next string: my_string = "weekend". What will return the next sintaxe: my_string[::-1]

my_string = "weekend"
print("my_string = ", my_string[::-1])

# You have the next lista: my_list = ['elem1', 'elem2', 44.5, [25, 41, 'python'], 999].
# How can you accees the string "python"

my_list = ['elem1', 'elem2', 44.5, [25, 41, 'python'], 999]
lista_index_4 = my_list[3][2]
print("The string is:", lista_index_4)

# For the string sir = "telecad", what output will you have if you run "sir[3]"?
sir = "telacad"
print(sir[3])

# For the string sir = "telacad", what output will you have if you run sir[:-1]?
print(sir[:-1])

# Which is the result after the run:
# >>>sir=”telacad”
# >>>sir.replace(“acad”,”emedicina”)
sir.replace("acad","emedicina")
print("sir = ", sir.replace("acad","emedicina"))

# Which is the final value of t after the run?
# >>>t=”telacad, academie, cursuri”
# >>>t =  t.split(',')
string_3_elements = "telacad, academie, cursuri"
string_3_elements = string_3_elements.split(',')
print(string_3_elements)

# Which is the final valuew of s after the run?
# >>>s=”telacad\n”
# >>>s = s.strip()
s="telacad\n"
s = s.strip()
print("S = ", s)

#  What will display the next sintaxa?
# >>> t = ""
# >>> if len(t) == 0:
# ...     print("the string t is empty")
# ...

t = ""
if len(t) == 0:
    print("the string t is empty")

# Which is the result of you run:
# >>>u=”email Bc@demy”
# >>>u.upper()

u="email Bc@demy"
u = u.upper()

print("u = ",u)

# Which is the result if you run:
# >>>ls=”SALUTARE, Vlad Lastname”
# >>>ls.lower()

ls = "SALUTARE, Vlad Lastname"
ls = ls.lower()
print("ls =", ls.lower())

# Which is the result if you run:
# >>>cap = "welcome to my github"
# >>>cap.capitalize()

cap = "welcome to my github"
cap = cap.capitalize()

print("cap =", cap)

# Which is the result if you run:
# >>>str1 = "how are you?"
# >>>print(str1[::-1])

str1 = "how are you?"
print(str1[::-1])

# Which is the result if you run:
# >>> t = [1, 3, 5]
# >>> len(t)

t = [1, 3, 5]
print(len(t))

# Which is the result if you run
# >>> t = [1, 3, 5]
# >>> t[2] = 4
# >>> t

t = [1, 3, 5]
t[2] = 4
print("t =", t)

# Which is the content of the lista t if you run:
#  >>> t = [1, 3, 4]
# >>> t.append("NI")

t_1 = [1, 3, 4]
print("t_1 =", t_1)
t_1.append("NI")
print("t_1 =", t_1)

# Which elements will containts the lista t if you run:
# >> t = [1, 3, 4]
# >>> t = t + [4,5,6]

t_3 = [1, 3, 4]
t_4 = t_3 + [4, 5, 6]
print("t_4 =", t_4)

# Which is the result if you run
# >>> t = [1, 3, 4]>
# >>> t.pop(2)
# >>> t

t_5 = [1, 3, 4]
t_5.pop(2)
print("t_5 =", t_5)

# Which order will the lista have if you will applay the function reverse?
# >>> my_list = [1, 9, 7]
# >>> my_list.reverse()
# >>> my_list

my_list = [1, 9, 7]
my_list.reverse()
print("my_list =", my_list)

# Which will be the order in the next lista if you applay the function "sort"?
# >>> my_list = [8, 17, -2, 11, 5]
# >>> my_list.sort()
# >>> my_list

my_list = [8, 17, -2, 11, 5]
my_list.sort()
print("my_list =", my_list)

# What will display the next secvence of code?
# >>> programming_language = "Python"
# >>> lista(programming_language)

programming_language = "Python"
print(list(programming_language))

#  What will display the next secvent of code?
# >>> my_list = [8, 17, 14, -8, 99, -25]
# >>> max(my_list) + min(my_list)

my_list = [8, 17, 14, -8, 99, -25]
print(max(my_list) + min(my_list))

# Which is the correct sintaxa to extract the element that is equal to "your name"
# >>> my_list = [8, 15, [23,14,69,[46,15,'your name']]]

my_list = [8, 15, [23, 14, 69, [46, 15, 'your name']]]
print("the wanted element =", my_list[2][3][2])