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

value_empty_list = bool([])
print("value_empty_list =", value_empty_list)

value_list = bool([1, 2, 3])
print("value_list [1, 2, 3] =", value_list)

value_empty_string = bool("")
print("value_empty_string =", value_empty_string)

value_string = bool("Vlad")
print("value_string =", value_string)

value_false_string = bool("False")
print("value_false_string =", value_false_string)
