"""
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
"""

mytuple = ("apple", "banana", "cherry")
print(mytuple)


# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")



thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))