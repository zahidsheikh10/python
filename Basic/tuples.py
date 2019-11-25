# A tuple is a collection which is ordered and unchangeable.
#  In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango");
print(thistuple);

# You can access tuple items by referring to the index number, inside square brackets
print("First item of tuple are :" +" "+thistuple[0]);

# Negative indexing means beginning from the end, -1 refers to the last item,
# -2 refers to the second last item etc

print("First item of tuple starting from end are:"+" "+thistuple[-1]);


# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# The search will start at index 2 (included) and end at index 5 (not included).

text = "The 2nd,3rd and 4th item of tuple are:{}";
items = thistuple[2:5];
print(text.format(items));

# Specify negative indexes if you want to start the search from the end of the tuple
# The below example returns the items from index -4 (included) to index -1 (excluded)
text1 = "The ist, 2nd and 3rd item of tuple from end are:{}";
items1 = thistuple[-4:-1];
print(text1.format(items1));

# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. 
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Convert the tuple into a list to be able to change it

convertTuple = ("apple","banana","kiwi");
convertedList = list(convertTuple);
convertedList[1] = "pineapple";
newTuple = tuple(convertedList);
text2 = "Items after modified in tuple are : {}";
print(text2.format(newTuple));


# You can loop through the tuple items by using a for loop.
for item in convertTuple:
    print(item);


# To determine if a specified item is present in a tuple use the in keyword
fruits = ("apple","banana","pineapple","orange","kiwi");
if "apple" in convertTuple:
    print("Yes, 'apple' is in the fruits tuple")


# To determine how many items a tuple has, use the len() method
lenght = len(fruits);
fruitsLength = "The length of fruits tuple are : {}";
print(fruitsLength.format(lenght));

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
del fruits;

# To join two or more tuples you can use the + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# It is also possible to use the tuple() constructor to make a tuple.
newTuple = tuple(("peas","carrot","ladyfinger","brinjal"));
vegetables = "The vegetable tuple are: {}"
print(vegetables.format(newTuple));


# Python has two built-in methods that you can use on tuples
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

fruits = ("apple","banana","pineapple","orange","kiwi");
numberOfApples = fruits.count("apple");
print(numberOfApples);

indexOfApple = fruits.index("apple");
print(indexOfApple);
