# Strings are created with " or '
print ("Hello " + 'world!')   #   Hello world!
print ("Hello" "world!")      #   Helloworld!

# A string can be treated like a list of characters
st="Hello World!"
print(st[0])        # H

# You can find the length of a string
print(len("This is a string"))


# Since Python 3.6, you can use f-strings or formatted string literals.
name = "Neehit"
print(f"She said her name is {name}." )

# Any valid Python expression inside these braces is returned to the string.
print(f"{name} is {len(name)} characters long.")

# None is an object
print(None)

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
print("etc" is None)    # False
print(None is None)     # True

#######################################################
#####      2. VARIABLES AND COLLECTIONS          #####
#######################################################

# By default the print function also prints out a newline at the end
# Use the optional argument 'end' to change the end string.
print("Hello, World", end="!!!") #'end' will not allow the next string from a new separate line.
print("\nHello, World\nNew world") # New Line
print('''Ohh Hello!
Are you there?         # Here double quotes three times will also work
Let's do some fun!!''')# Multi-line string / Paragraph


# Simple way to get input data from console
'''input_string_var = input("Enter some data: ")
print(input_string_var)'''


# There are no declarations, only assignments.
# Convention in naming variables is snake_case style.
some_var = 5
print(some_var)

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
'''
try:
  # This variable doesn't exist yet!
  print(secret_code)
except NameError:
  #Python jumps straight here instead of crashing
  print("Oops! That variable hasn't been created yet. Setting a default...")
  secret_code = "1234"
  print(f"New code set:{secret_code}")
  
########### One More Example of try and except
# Exceptional Handling with 'else' and 'finally'
# 'else will run only when the block executed perfectly without any errors.
# 'finally' will be running always




try:
  num = int(input("Enter a number: "))
  result = 10 / num
except ZeroDivisionError:
  print("You can't divide by zero!")
except ValueError:
  print("That wasn't a valid number!")
else:
  print(f"Success! The result is {result}")
finally:
  print("This code runs no matter what happens above.")
'''



# 'if' can be used as an expression
# Equivalent 
print("yay!") if 5 > 1 else print("nay!")