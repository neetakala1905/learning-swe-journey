## Sets
empty_set = set()   # 
# Initialize a set with a bunch of values.
some_set = {1, 1, 2, 3, 3, 2, 4}
print(some_set) # {1, 2, 3}

# Elements of a set have to be immutable
# invalid_set = {[1], 1} ## TypeError: unhashable type : 'list'
valid_set = {(1,), 1}
print(valid_set)

# Add one more item to the set
filled_set = some_set
filled_set.add(5)
# Sets do not have duplicate elements
filled_set.add(5) # it remains the same as before

# do set intersection with &
other_set = {3, 4, 5, 6}
print(filled_set & other_set)

# do set union with |
print(filled_set | other_set)

# Do set symmetric difference with ^
print(filled_set ^ other_set)

# Do set difference with -
print(filled_set - other_set)

# Check if set on the left is a superset of set on the right
print({1, 2, 3} >= {1, 2, 3, 4, 5, 6, 7})

# Check if set on the right is a superset of set on the right
print({1, 2, 3} <= {1, 2, 3, 4, 5, 6})

# Check for the existence in a set with 'in'
print("2 is there" if (2 in filled_set) else "2 is not there")
print(11 in filled_set)
