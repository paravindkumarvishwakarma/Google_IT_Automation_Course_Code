"""
Comparison expressions return a Boolean result (True or False). 

x == y        If x is equal to y, return True. Else, return False.

x != y         If x is not equal to y, return True. Else, return False.

x < y          If x is less than y, return True. Else, return False.

x <= y        If x is less than or equal to y, return True. Else, return False.

x > y          If x is greater than y, return True. Else, return False.

x >= y        If x is greater or equal to y, return True. Else, return False.
"""


#Skill Group 1
#Use a comparison operator with numbers
#Use a comparison operator to alphabetize strings

# The value of 10*4 (40) is greater than 14+23 (37), therefore this 
# comparison expression will return the Boolean value of True.


print(10*4 > 14+23) # Should print True

# The letter "t" has a Unicode value of 116 and the letter "s" has a
# Unicode value of 115. Since 116 is not less than 115, the 
# comparison of "tall" < "short" (or 116 < 115) is False. 

print("tall" < "short")  # Should print False



#Skill Set 2
"""
    Use a function with the def() keyword

    Pass a parameter to the function

    Use an if-elif-else statement

    Assign strings to variables 

    Use conditional operators

    Return a value
"""

# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server


#Skill Set 3
"""
Use an if-elif-else statement with:

    comparison operators

    logical operators
"""
# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.


#Skill Set 4
"""
    Use an if statement to calculate a return value

    Use conditional operators

    Recall the arithmetic operators // and %
"""

# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
# The floor division operator will calculate the integer value of
# "number" divided by x: 35 // 10 will return the integer 3.
  whole_number = number // x
# The modulo operator will calculate the remainder value of "number"
# divided by x: 35 % 10 will return the remainder value 5.
  remainder = number % x
# If the remainder is greater than or equal to 5: 
  if remainder >= 5: 
# Return x multiplied by the (whole_number+1) to round up
    return x*(whole_number+1)
# Else, return x multiplied by the whole_number to round down
  return x*whole_number
 
# Calls the function with the parameter value of 35.
print(round_up(35)) # Should print 40



#########################QUIZE RELATED TO CONDITIONAL STATEMENT###############################

#Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

#What’s the output of this code if number equals 10?
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

#Output = 3
  


###################Graded Quize#################
################################################

#Skill Group 1
print("Skill Group 1")
"""
Use a function with the def() keyword

Pass a parameter to the function

Use an if-elif-else block to set specific conditions for a variety of actions

Assign strings to variables 

Use comparison operators

Return a value

Call the function in a print statement and pass parameter to the function
"""
# A function is created with the def() keyword. The parameter
# variable "time_as_string" is passed to the function through a 
# call to the function.
def task_reminder(time_as_string):

    # The following if-elif-else block assigns various strings to
    # the variable "task" depending on specific conditions. The
    # test conditions are set using the == equality comparison 
    # operator. In this case, the time passed through the 
    # "time_as_string" parameter variable is tested as the 
    # specific condition. So, if the time  is "11:30 a.m.", then 
    # "task" is assigned the value: "Run TPS report".
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    # The else statement is a catchall for all other values of 
    # the "time_as_string" parameter variable not listed in the
    # if-elif block of code.
    else:
        task = "Provide IT Support to employees"

    # This line returns the value of "task" to the function call.
    return task

# This line calls the function and passes a parameter  
# ("10:00 a.m.") to the function.
print(task_reminder("10:00 a.m."))
# Should print "Provide IT Support to employees"

#---------------------OUTPUT----------------
#Provide IT Support to employees



#Skill Group 2
print("Skill Group 2")
"""
Predict the output of expressions written with Python’s syntax. 

Requires an understanding of:

  Arithmetic and logical operators 

  How functions return and print values

  How if-elif-else statements work

  Comparison operators
"""

# Example 1
# Evaluate the output of this print statement

def product(a, b):
        return(a*b)

print(product(product(2,4), product(3,5)))
 
#################################

# Example 2 
# Evaluate the output of this print statement

def difference(a, b):
        return(a-b)

def sum(a, b):
        return(a+b)

print(difference(sum(2,2), sum(3,3)))


#################################


# Example 3
# Evaluate the Boolean output of this comparison


print((5 >= 2*4) and (5 <= 4*3))


#################################


# Example 4 
# Evaluate the value of the comparison in the if statement 


x = 3
if x+5 > x**2 or x % 4 != 0:
        print("This comparison is True")


#################################


# Example 5 
# Evaluate the output of this if-elif-else statement


number = 6
if number * 2 < 14:
        print(number * 6 % 3)
elif number > 7:
        print(100 / number)
else:
        print(7 - number)


# Click Run to check your answers. If you are having trouble 
# calculating the correct answers manually, please review the
# Practice Quiz Study Guides, videos, and readings in this Module.


#Skill Group 3
print("Skill Group 3")
"""
Create an if-elif-else statement with: 

  a complex conditional statement using both comparison and logical operators

  values assigned to variables 

  arithmetic operators, including the modulo % operator
"""
def get_remainder(x, y):
 
  if x == 0 or y == 0 or x ==y:
    remainder = 0
  else:
    remainder = (x % y) / y
  return remainder


print(get_remainder(10, 3))

