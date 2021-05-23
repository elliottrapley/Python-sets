# Set items are enclosed in curly brackets
# Set is unordered
# Set is mutable, can contain only immutable items
# Set elements are unique
# Elements can contain only immutable items

"""
Sets can be used for mathematical set operations such as union, intersection, difference 
and symmetric difference.

https://en.wikipedia.org/wiki/Set_(mathematics)
"""

"""
Python Set Attributes
"""

print(dir(set))

"""
Creating Python Sets
"""

# integers
set = {1, 2, 3}
# mixed data types
set = {3.2, "Hi", (1, 2, 3)}
# Distinguish set and dictionary while creating an empty set

# initialize a with {}
empty = {}
print(type(empty))  # Output => <class 'dict'>
# initialize a with set()
empty = set()
print(type(empty))  # Output => <class 'set'>

"""
Modifying a set in Python
"""

set_example = {"hello", "world"}
# you cannot call using indexing
# TypeError: 'set' object is not subscriptable
set_example[0]
# using add() method
# output => {'hello', 'yay!', 'world'}
set_example.add("yay!")
print(set_example)
# list is mutable, cannot be used.
# TypeError: unhashable type: 'list'
set_example.add(["hello", "world"])
# using update() method
# add multiple elements
# using different data types
# output => {1, 2, 'yay!', 3, 4, 5, 6, 7, 8, 'world', 'hello'}
set_example.update([1, 2, 3], {4, 5, 6}, (7, 8,))
print(set_example)


"""
Removing elements from a set
"""

set_example = {1, 3, 4, 5}
# discard an element
# output => {1, 4, 5}
set_example.discard(3)
print(set_example)
# discard element not present
# no errors raised
set_example.discard(30)
# remove an element not present
# KeyError: 30
set_example.remove(30)
set_example = {1, 3, 4, 5, 6}
# pop an element
# output => random element
set_example.pop()
print(set_example)
# pop another element
# output => random element
set_example.pop()
print(set_example)
# clear the set
# output => set()
set_example.clear()
print(set_example)

"""
Set Union Operations
"""

a = {1, 2, 3}
b = {4, 5, 6}
# using | operator
# output => {1, 2, 3, 4, 5, 6}
print(a | b)
# use union () function
# output => {1, 2, 3, 4, 5, 6}
print(a.union(b))

"""
Set Intersection Operations
"""

a = {1, 2, 3, 6, 7}
b = {4, 5, 6, 7, 8, 9}

# using & operator
# output => {6, 7}
print(a & b)

# use the intersection operator
# output => {6, 7}
print(a.intersection(b))

"""
Set Difference Operations
"""

a = {1, 2, 3, 6, 7, 9}
b = {4, 5, 6, 7, 8, 9}

# using - operator
# output => {1, 2, 3}
print(a - b)

# using - operator
# output => {8, 4, 5}
print(b - a)


# using difference() function
# output => {1, 2, 3}
print(a.difference(b))

"""
Set Symmetric Difference
"""

a = {1, 2, 3, 6, 7, 9}
b = {4, 5, 6, 7, 8, 9}
# using ^ operator
# output => {1, 2, 3, 4, 5, 8}
print(a ^ b)
# using symmetric_difference method
# output => {1, 2, 3, 4, 5, 8}
print(a.symmetric_difference(b))

"""
Set Methods
"""

# add() - Adds an element to the set
# clear() - Removes all the elements from the set
# copy() - Returns a copy of the set
# difference() - Returns a set containing the difference between sets
# difference_update() - Removes the items in this set that are also in another
# discard() - Remove the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes items in a set that are not present in other
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() - Returns a set with the symmetric differences
# symmetric_difference_update() - inserts the symmetric differences
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others