#A Closer Look at the Range() Function
"""
The in keyword, when used with the range() function, generates a sequence of integer numbers, which can be used with a for loop to control the start point, the end point, and the incremental values of the loop.  

Syntax-----------
for n in range(x, y, z):
    print(n)


The range() function uses a set of indices that point to integer values, which start at the number 0. The numeric values 0, 1, 2, 3, 4 correlate to ordinal index positions 1st, 2nd, 3rd, 4th, 5th. So, when a range call to the 5th index position is made using range(5) the index is pointing to the numeric value of 4.
Index Number    1st index   2nd index  3rd index  4th index  5th index
Value              0           1          2          3          4

The range() function can take up to three parameters:  range(start, stop, step) 

1. Start 
    The first item in the range() function parameters is the starting position of the range. The default is the first index position, which points to the numeric value 0. This value is included in the range. 

2. Stop
    The second item in the range() function parameters is the ending position of the range. There is no default index position, so this index number must be given to the range() parameters. For example, the line for n in range(4) will loop 4 times with the n variable starting at 0 and looping 4 index positions: 0, 1, 2, 3. As you can see, range(4) (meaning index position 4) ends at the numeric value 3. In Python, this structure may be phrased as “the end-of-range value is excluded from the range.” In order to include the value 4 in  range(4), the syntax can be written as range(4+1) or range(5). Both of these ranges will produce the numeric values 0, 1, 2, 3, 4. 

3. Step
    The third item in the range() function parameters is the incremental step value. The default increment is +1. The default value can be overridden with any valid increment. However, note that the loop will still end at the end-of-range index position, regardless of the incremental value. For example, if you have a loop with the range: for n in range(1, 5, 6), the range will only produce the numeric value 1. This is because the incremental value of 6 exceeded the ending point of the range.


"""

#Test Case 1
#Range(3)
for x in range(3):
    print(x)

#Range(3+1)
for x in range(3+1):
    print(x)

#Test Case 2
#range(start, stop)
#range(2,6)
for x in range(2,6):
    print(x)

#range(5,10+1)
for x in range(5, 10+1):
    print(x)

#Test Case 3
#range(start, stop, step)
for x in range(4, 15+1, 2):
    print(x)

#range(4, 15+1, 2)
for x in range(4, 15+1, 2):
    print(x)

#range(2*2, 25, 3+2)
for x in range(2*2, 25, 3+2):
    print(x)

#range(10, 0, -2)
for x in range(10, 0, -2):
    print(x) 

#range(1, 5, 6)
for n in range(1, 5, 6):  
    print(n)

#Example of the range() function in code:
    
#Example 1
