mytuple = tuple(['Max', 28, "Boston"])
print(mytuple)

# getting a particular item in the tuple
item = mytuple[0]
print(item)

# changing a particular element in the tuples
# mytuple[0] = "twinMartin"
# not possible because a tuple is immutable

# printing all elements in the array
for x in mytuple:
    print(x)

# checking for particular element in the array
if "Max" in mytuple:
    print("max is here")
else:
    print("max is not here")

# finding number of elements in the tuples
print(len(mytuple))

# find the numbr of a certain letter in the tuple
print(mytuple.count('m'))

# checking index of an element
print(mytuple.index(28))

# converting tuple to list
mylist = list(mytuple)
print(mylist)
# convert back to tuple
mytuple2= tuple(mylist)
print(mytuple2)

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[3:6]
print(b)

# skipping elements
c = a[::2]
print(c)