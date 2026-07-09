#################################################
######## 3. Control Flow and Iterables ##########
#################################################

some_var = 5

# Identation is significant in Python!

if some_var > 10:
  print("Hey, Greater than 10.")
elif some_var < 10:
  print("Hey, Smaller than 10.")
else:
  print("It's equals to 10.")
  
  
# Match / Case - Introduced in Python - 3.0
# It compares a value against multiple conditions and executes the matching case block.
'''
command = input("Enter your command!   ")

match command:
  case "run":
    print("The robot started running 🏃")
  case "speak" | "say_hi":
    print("The robot said hi 🗣️")
  case code if command.isdigit(): # conditional, assume that code is a greedy variable, eager to take all the values
    print(f"The robot execute coe: {code}")# but, it will only accept the numbers.
  case _:
    print("Invalid command ❌")
 
 '''   

# For loop using 'range'
for x in range(2):
  print(x)
  
# For loops over lists
for fruit in ["Mango", "Apple","banana"]:
  print(fruit)
  
veggies = ["brinjal", "tomato", "potato", "ginger"]
for i, value in enumerate(veggies):
  print(value, i)
  
i = 1
while i <= 4:
 print(i)
 i += 1
 
