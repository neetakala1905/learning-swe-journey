# Tuples are like lists but are immutable.
# If you try to use list methods of adding or removing the element
# Then Python will throw an error 'AttributeError'
tup = (1, 2, 3)
print(tup[0])

# The below line is going to give you the 'TypeError'
# Because 'tuples' are immutable i.e. once the value is give can not be changed
# tup[0] = 4



# Note that a tuple of length one has to have a comma after the last element but 
# If tuples of other lengths, even zero do not.
print(type((1)))  # <class 'int'>
print(type((1, ))) # <class'tuple'>
print(type(())) # <class 'tuple'>

# We can do most of the list operations on tuples too
print(len(tup))
print(tup + (4, 5, 6))
tup[:2]  # (1, 2)
print(2 in tup)



# We can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)
print(a, c, b)

# We can also do extended unpacking
a, *b, c = (1, 2, 3, 4)
print(a, b, c) # (1, ,[2, 3], 4)

# Tuples are created by default if we leave out the parentheses
d, e, f = 4, 5, 6 # tuple 4, 5, 6 is unpacked into variables d, e, f

# Now we can see how easy it is to swap two values
e, d = d, e # d is now 5 and e is now 4
print(d, e, f)


# Dictionaries store mappings from keys to values
empty_dict = {}
filled_dict = {"one": 1, "two":2, "three": 3}

# Immutable types include ints, floats, strings, tuples.
'''invalid_dict = {[1, 2, 3]: "123"}
print(invalid_dict)''' # Here we can see that key cannot be a list.
# Because list are mutable and keys must not be modified

valid_dict = {(1, 2, 3):[1, 2, 3]} # Values can be of any type
print(valid_dict)


# Look up values with [], we need to provide it a key.
print(filled_dict["one"]) # 1


# In Python 3.7 or + will be maintaining the order of the dictionary
# Rest of them may give a different order as compared to the assigned one.



# Get all the keys as an iterable with "keys()". We need to wrap the call in list()
print(list(filled_dict.keys()))


# Get all the values
print(list(filled_dict.values()))


# Check for the existence of the keys in a dictionary with "in"
print("one" in filled_dict) # True
print(1 in filled_dict) # False, it is for the key only 

# Looking up a non-existing key is a KeyError
# filled_dict['four']   # KeyError

# Use 'get()' method to avoid the KeyError
print(filled_dict.get("one"))     # 1
print(filled_dict.get("four"))     # None


# The'get()' method supports a default argument when the value is missing
print(filled_dict.get("one", 4))    # 1
print(filled_dict.get("four", 4))   # 4


# 'setdefault() inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)
filled_dict.setdefault("five", 6) # This will not work, since it worked for the key and 
#set the value for the key 'five' to 5, now it will not change by this way.
print(filled_dict)


# Adding to a dictionary
filled_dict.update({"four":4})
# Another Way to a add an element
filled_dict["six"] = 6
print(filled_dict)


#Deleting a value
del filled_dict['six']
print(filled_dict)

# A new dictionary
user = {"name": "Alice", "role":"admin"}

#Updating an existing value
user["name"] = "Neeta"
user["role"] = "Super Admin"

#Adding a brand-new key-value pair
user["status"] = "value"

print(user)