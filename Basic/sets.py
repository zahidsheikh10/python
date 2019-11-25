# A set is a collection which is unordered and unindexed. 
# In Python sets are written with curly brackets
# Create a Set

thisset = {"apple", "banana", "cherry"}
print(thisset)

# You cannot access items in a set by referring to an index, 
# since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
# by using the in keyword

for items in thisset:
    print(items);


# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

thisset.add("pineapple");
print(thisset);

# To add more than one item to a set use the update() method.
thisset.update(["orange","kiwi"]);
print(thisset);

# To determine how many items a set has, use the len() method
print(len(thisset));

# To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana");
print(thisset);


# You can also use the pop(), method to remove an item, 
# but this method will remove the last item. Remember that sets are unordered, 
# so you will not know what item that gets removed.
# The return value of the pop() method is the removed item
# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

thisset.pop();
print(thisset);

# The clear() method empties the set
thisset.clear();
print(thisset);

# The del keyword will delete the set completely
del thisset;
# print(thisset);


# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, 
# or the update() method that inserts all the items from one set into another

# The union() method returns a new set with all items from both sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {5, 6, 7};
set1.update(set2);
print(set1);

# It is also possible to use the set() constructor to make a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)