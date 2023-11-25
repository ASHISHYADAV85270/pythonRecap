fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
'''list are mutable means elements can be changed but string 
 are not mutable '''
newlist = []

for x in fruits:
  if "a" in x:
    fruits.remove(x)
    newlist.append(x)


fruits.sort()
newlist.reverse()
print(fruits)
print(newlist)