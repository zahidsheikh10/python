#The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.
#  Add an element to the fruits set

fruits = {"banana","pineapple","cherry"};
fruits.add("apple");
print(fruits);


# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "pineapple"}
z = x.difference(y)
text = "The set items which are present in set x but not in set y are: {}"; 
print(text.format(z));

# The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, 
# or in all sets if the comparison is done with more than two sets.

intersection = x.intersection(y);
text = "The set items which are present in both set x and set y are: {}"; 
print(text.format(intersection));


# The isdisjoint() method returns True if none of the items are present in both sets, 
# otherwise it returns False.
similar = x.isdisjoint(y);
text = "Is x and y disjoint sets means do that have any element in common:{}"
print(text.format(similar));


# The issubset() method returns True 
# if all items in the set exists in the specified set, otherwise it retuns False.
a = {"a","b","c","d","e"};
b= {"a","b","c","d","e","f","g"};
text = "Is set a sub set of set b means all the elements of set a are present in set b: {}";
subset = a.issubset(b);
print(text.format(subset));


# The issuperset() method returns True 
# if all items in the specified set exists in the original set, otherwise it retuns False.