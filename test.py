'''
take_it = input("Enter the command")
match take_it:
  case "do":
    print("Robot start doing this")
  case "don't" | "leave":
    print("Robot will not follow it.")
  case _:
    print("Invalid command")
    
  
    
stuff = ["toys", "chocolate", "milk", "cream", "yogurt"]

for i, value in enumerate(stuff):
  
  print(i, value)
  
i = 1
while i <=4:
  print(i)
  i += 1
  
    '''


try:
  num = int(input("Enter the number   "))
  result = 10 / num
except ZeroDivisionError:
  print("The number cannot be divided by zero")
except (ValueError, TypeError):
  print("Type a valid number")
else:
  print(f"The result is {result}")
finally:
  print("I will always be there, no matter what!!")