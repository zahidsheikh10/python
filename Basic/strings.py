a = """This is a multi line string example""";
print(a);

# Strings are Arrays
a = "Hello, World!"
print('The character at position 2 is ' + a[1])

# Slicing
# we can return a range of characters by using the slice syntax.

b = "Hello, World!"
print("The characters of string b from position 2 - 5 excluding 5th position , starting from begining are :  "+ b[2:5]);

# we can use negative indexes to start the slice from the end of the string:
print("The characters of string b from position 2 - 5 excluding 5th position , starting from end are : "+ b[-5:-2]);

# To get the length of a string, use the len() function.
length = len(b);
text = "The lengt of string b is {}";
print(text.format(length));


# The strip() method removes any whitespace from the beginning or the end
z = " Hello, World! "
print(z.strip()) # returns "Hello, World!"

# The lower() method returns the string in lower case:
print("Print string z in lower case :" + z.lower());

# The upper() method returns the string in upper case:
print("Print string z in upper case :" + z.upper());

# The replace() method replaces a string with another string:
print("Replacing the letter h to j in string z"+ z.replace("H","J"));

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(",")) # returns ['Hello', ' World!']