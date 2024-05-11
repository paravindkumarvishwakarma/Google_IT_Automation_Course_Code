def greeting(name):
    print("Welcome, " + name)
    
greeting("Suraj")
greeting("Pwana")

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Paravind", "Software engineering")
greeting("Suraj", "Software engineering")
greeting("Pawan", "Software engineering")

def paravind(x,y):
    print(x+y)

paravind(5,3)

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b
print("The sum of both area is:", str(sum) )

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def greating(name):
    print("welcome, " + name)
result = greating("Paravind")
print(result)

name = "paravind" 
number = len(name) * 9
print("Hello" + name + ". Your lucky number is " + str(number))

name = "Pawan"
number = len(name) * 9
print("Hello" + name + ". Your lucky number is " + str(number))

#We can write above code in simple way using functions
def lucky_number(name): #Find the lucky number
    number = len(name) * 9
    print("Hello" + name + ". Your lucky number is " + str(number))

lucky_number("Paravind Kumar Vishwakarma")
lucky_number("Pawan Chaturvedi")

def calculate(d):
    q = 3.14
    z = q * (d**2)
    print(z)

calculate(5) #Output is 78.5

def circle_area(radius): #Find the area of circle
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5) #Outpur is 78.5

"""Skill Group 1

    Use a function that accepts multiple parameters

    Return a result value"""

# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))

"""Skill Group 2

    Use a function to return the result of a measurement conversion

    Use arithmetic operators to perform a calculation

    Combine text with a function call within a print() statement

    Convert the return value from a float data type to a string for the print() function

    Call the function and perform a calculation on the return value within a print() statement"""

# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in milliliters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in milliliters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in milliliters is " + str(convert_volume(4))

