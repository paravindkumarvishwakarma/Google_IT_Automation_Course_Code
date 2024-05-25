#Slicing and Joing strings
"""When you slice a string, you extract a subset of the original string—sometimes referred to as indexing a string. Joining strings is the process of linking two or more strings together to create a bigger string."""


#How to slice strings
"""Bracket notation, [ ], is used to specify the start of the index, ending index, or both. If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index. This is the same if you do not include the ending index. """

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[-10:]) # Prints “Earthlings” again
print(string1[55:]) # Prints “” 
print(string1[0::2]) # Prints “Getns atlns”
print(string1[::-1]) # Prints “sgnilhtraE ,sgniteerG”


#How to join strings
print("Hello" + " " + "world") #Prints “Hello world”

#You can also use the join() function, whixh is very useful when you want to concatenate element =s from a list of strings with a specific delimiter.
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

#You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"


#How to combine slicing and joining strings
# The first 3 digits are the area code:

