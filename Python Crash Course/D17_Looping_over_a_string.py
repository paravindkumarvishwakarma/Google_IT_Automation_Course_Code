#Looping over a string
"""
To loop over a string means to start with the first character in a string and iterate over each character until the end of the string. Strings are objects that contain a sequence of single-character strings. Yes, a single letter is classified as a string in Python. For example, string[0] is considered a string even though it is just a single character.
Note: Python does not use characters as a type like other programming languages do; it just supports strings with a length of 1.

"""
for i in range(len(greeting)):
	print(i)
	
"""
len(greeting) is an integer that tells Python how many characters are in the string. But because it’s an integer, you need to convert it to an iterable sequence by using the range() function. This loop does the same thing as the loop above, but instead of printing elements, it prints integers resulting in the output below:
0

1

2

3

4
"""


#While Loop with indexing
"""
This while loop is the more “common” while loop that programmers often use. This type of loop involves an index variable to represent the current position within the sequence. Most of the time, this will start with 0 for the initial iteration. Let’s take a look at an example:

"""
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
	
"""
The initial index value is 0, and the while loop continues to execute as long as the index variable is less than the length of the len(greeting). At each iteration, Python prints the value at the current index position (greeting[index]). Then, Python increments the index by 1 (index += 1) to move to the next position. The output of this example is:

H

e

l 

l 

o 
"""



#While loop with slicing
"""
Using a while loop with slicing accomplishes the same thing that a while loop with indexing does—like the example you explored above—this is just another way to write a while loop. You use this while loop in combination with string slicing to iterate over a portion of a sequence. Remember, it’s up to you to choose the method for looping over a string based on your level of comfort. There are multiple ways to write lines of code to execute the same result. Let’s explore how a while loop with slicing results in the same output.
"""
