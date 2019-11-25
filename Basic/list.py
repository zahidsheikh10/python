# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

# You access the list items by referring to the index number
# Print the second item of the list

print("The second element of list are:" + thislist[1]);

# Negative indexing means beginning from the end, -1 refers to the last item, 
# -2 refers to the second last item etc.
# Print the last item of the list

print("The last element of list are:" + thislist[-1] );

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item

print("The 3rd 4th and 5th item of list are:");
print(thislist[2:5]);

# This example returns the items from the beginning to "orange"
print(thislist[:4]);

# This example returns the items from "cherry" and to the en
print(thislist[2:]);

# Specify negative indexes if we want to start the search from the end of the list
print(thislist[-4:-1]);

# To change the value of a specific item, refer to the index number
thislist[1] = "blackcurrant";
print(thislist);

# You can loop through the list items by using a for loop
for item in thislist: 
    print(item);

# To determine if a specified item is present in a list use the in keyword
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

#To determine how many items a list has, use the len() function
txt = "The length of list are {}";
length = len(thislist);
print(txt.format(length));

# To add an item to the end of the list, use the append() method
thislist.append("pineapple");
print(thislist);

# To add an item at the specified index, use the insert() method
thislist.insert(0,"Delicious Apple");
print(thislist);

# The remove() method removes the specified item
thislist.remove("orange");
print(thislist);

# The pop() method removes the specified index, (or the last item if index is not specified
thislist.pop();
print(thislist);

# The del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely
del thislist;
# print(thislist);

# The clear() method empties the list
thislist = ["apple", "banana", "cherry"];
thislist.clear();
print(thislist);

# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().

# Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list()
# Make a copy of a list with the list() method

mylist = list(thislist)
print(mylist)

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [5, 6, 7]

for x in list2:
  list1.append(x)

print(list1)

# you can use the extend() method, which purpose is to add elements from one list to another list
list1 = ["a", "b" , "c"]
list2 = [8, 9, 10]

list1.extend(list2)
print(list1)

# It is also possible to use the list() constructor to make a new list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# we can sort the list using the sort() method
print(thislist.sort());