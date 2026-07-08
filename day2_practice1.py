# Single line comments start with a number symbol.

"""" Multiline string can be written
    using three "s, and are often used
    as documentation.
"""
#####################################
#1. Primitive Datatypes and Operators
#####################################

# You have numbers
3 # => 3

# Maths is always there
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 7 # => 5

# Decimal Value
print(-10 / 3, "division")

# Floor division rounds towards negative infinity
# Floor means 'less than or equals to that number
5 // 3      # => 1
-5 // 3     # =>-2
5.0 //3.0   # =>1.0
print(5.0 // -3.0) # =>-2.0

# This makes a difference
print(int ( -5 / 3 ), "integer conversion")


# The result of division is always a float
print(10 / 3)
10.0 / 3    # This will be giving you a float value




#Important
# Modulo operation
# Formula => a % b = a - (a // b) * b


print(5 % 3, "Modulo")    # => 2
# What happened here => 5 - (1)* 3 = 5 - 3 => 2


print(-5 % 3)
# i % j have the same sign as j
# Here => -5 -(-2 * 3) => -5 + 6 => 1

print(5 % -3) # The result will be -1
# i % j have the same sign as j

print(-5 % -3) # => -2
# Here => -5-(1 * -3) => -2

# Now dealing with simple stuff
print(5 % 5)
print(10 % 3)

# Exponential (x**y, x to the yth power)2^3
2**3 # => 8

# Enforce precedence with parentheses
1 + 3 * 2     # => 7
(1 + 3) * 2   # =>8

# Boolean values are primitives (Note : the capitalization)
True
False

# Negate with not
not True # => False
not False # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False    # => False
False or True    # => True

# True and False are actually 1 and 0 but with different keywords
print("Boolean Maniputlations With Numbers")
print(True + True)  # => 2
print(True * 8)     # => 8
print(False - 5)    # => -5

# Comparison operators look at the numerical Value of True and False
0 == False  # =>True
2 > True  # =>True
3 == True # =>False
-5 != False # =>True

# None, 0, and empty strings / lists / dicts / tuples / sets, all evalutes to False.
# All other values are True
print("Boolean Operations")
print(bool(0))     # => False
print(bool(""))     #  => False
print(bool([]), bool({}), bool(()))     #  => False
print(bool(set()))      #  => False
print(bool(4))      # => True
print(bool(-6))     # => True


# Using Boolean logical operators on ints, casts them to boolean for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and / or (&, |)
print("Some more operations")
print(bool(0)) # => False
print(bool(2)) # => True
print(0 and 2) # => 0
print(bool(-5)) # => True
print(bool(-5 or 0))  # => True


# Equality is ==
# Inequality is !=
print("EQUAL OR INEQUALITY")
print(1 == 1)   # => True
print(2 != 1)   # => True

print("More comparisons")
print(1 < 10)   # => True
print(1 > 10)   # => False
print(1 <= 1)   # => True
print(1 >= 1)   # => True


print("Seeing whether a value is in a range")
print(1 < 2 and 2 < 3)  # => True
print(2 < 3 and 3 < 2)  # => False

print("Chaining")
print(1 < 2 < 3)    # => True
print(1 < 2 > 3)    # => False






