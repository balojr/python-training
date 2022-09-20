mylist = ["martin", "thug", "slime"]
print(mylist)

# printing elements in the list
for x in mylist:
    print(x)

# checking if an element is present in a list
if "thug" in mylist:
    print("thug is here")
else:
    print("thug outta here")

print(len(mylist))

# appending items in a lists
mylist.append("wheezy")
print(mylist)

# inserting item at a specific position
mylist.insert(2, "gunna")
print(mylist)

# removing items using pop method
item = mylist.pop() 
#  you can pop a specific element on the list by inserting the index in the pop method
print(item)
print(mylist)

# removing elements using the remove method
item = mylist.remove("gunna")
print(mylist)

# removing all items using the clear method
# item = mylist.clear()
# print(mylist)

# reversing the list using the reverse method
item = mylist.reverse()
print(mylist)

# sorting list using the sort method (works mostly using numbers)
mylist.sort()
print(mylist)

# sorting a list and creating a new one in the sorted order
mylist.sort()
new_list = sorted(mylist)
print(mylist)
print(new_list)

# 2 lists can be added using the + operator
mylist2 = new_list + mylist
print(mylist2)

# displaying certain elements in a list
thelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# using the start index and stop index
a = thelist[1:5]
print(a)
# using the step method
b = thelist[::2]
print(b)

# copying a list
thelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_cpy = thelist.copy()
list_cpy.append("martin")
print(list_cpy)
print(thelist)
# or
thelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_cpy = list(thelist)
list_cpy.append("martin")
print(list_cpy)
print(thelist)

# list comprehension. or creating a list from an existing list
thelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squaredlist = [x*x for x in thelist]
print(mylist)
print(squaredlist)