# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]
print(other_li, li)


# Add stuff to the end of a list with append
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)

print(li)

#Remove from the end with pop
li.pop()
print(li)

# Access a list like you would have done with array
print(li[0])

# Look at the last element
# Direct accessing to the last element without getting the length of the string
print(li[-1])

# Looking out of bounds is an IndexError
# li[4]   # Raises an IndexError

# You can look at ranges with slice syntax.
# The left value from colon is included and the right one is not it's like n-1
# It's a closed / open range for you mathy types.
print(li[0:4])    # [1, 2, 3, 4]
print(li[2:])     # [3, 4]
print(li[:3])     # [1, 2, 3]
print(li[::2])    # Return list selecting elements with a step size of 2 = > [1, 3]
print(li[::-1])   # Return the list in reverse order
# Syntax => list_name[start:end:step]


# Make a shallow copy using slices
li2 = li[:]   # => li2 = [1, 2, 4, 3] but (li2 is li) will be FALSE.
print(li2 is li)

li3 = li
print(li3 is li) # Now this is 'True'

# Remove random / choice based elements from a list with "del"
del li[2]
print(li)

# Remove first occurrence of a value
li.remove(2)
print(li)

# li.remove(2) # This will raise a 'ValueError' as 2 is not there.


# Insert an element at a specific index
li.insert(1, 2) # lis is now [1, 2, 3]
print(li) # because of the above line, 2 is inserted at the index of 1


# To get the index of the first item found matching the argument
print(li.index(4))
# print(li.index(3)) # There is no such value available in the list
# The above line will raise 'ValueError'


# You can add lists
# '+' operator will not modify, any of them, they remains as it is
print(li + other_li)

# Concatenate lists with "extend()"
# There is a difference between the '+' operator and the extend()funtion
# extend() will modify the 'li'
li.extend(other_li)
print(li)



# Check for existence in a list with "in"
print(1 in li ) # True

# Examine the length with "len()"
print(len(li))

