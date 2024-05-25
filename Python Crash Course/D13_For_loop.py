#What is For loop
# Ans = Iterates over a sequence of values

#All About Range
"""
1. In Python, and a lot of other programming languages, a range of numbers will start with the value '0' by default.
2. The list of numbers generated will be one less than the given value.
"""

#Where for loop and where while loop?
"""
1. Use for loops when there's a sequence of elements that you want to iterate
2. Use while loops when you want to repeat an action until a condition changes.
"""

"""
for x in range(5):
    print(x)
"""

#Type 1
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)


#Type 2
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))

#Example 1 
print("Example 1 Output")
product = 1
for n in range(1,10):
  product = product * n

print(product)
print("\n")

#Example 2
print("Example 2 Output")
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))


#Example of for loop with the in keyword and the range() function
# This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to it to include 6 in the range). The incremental value
# for the loop is 2 (number+2). The print() function will output the
# resulting value of "number" multiplied by 3.

for number in range(1, 6+1, 2):
    print(number * 3)

# The loop should print 3, 9, 15
    

#Commin pitfalls when using the range() function
# This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print() 
# function will output the resulting value of "number" squared.

for number in range(2,8):
    print(number**2)

# The loop should print 4, 9, 16, 25, 36, 49


#Nested for loop
# This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")


#for loop with nested if statement
# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)



