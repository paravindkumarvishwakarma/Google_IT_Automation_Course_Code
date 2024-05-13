#Question 1
#Complete the code to output the statement, “Diego’s favorite food is lasagna”. Remember that precise syntax must be used to receive credit.
print("##############Solution 1#############")
name = "Diego"
fav_food = "lasagna"
print(name + "’s favorite food is " + fav_food) 
print("\n")

#Question 2
"""
Consider the following scenario about using if-elif-else statements:

Police patrol a specific stretch of dangerous highway and are very particular about speed limits.  The speed limit is 65 miles per hour. Cars going 85 miles per hour or more are given a “Reckless Driving” ticket. Cars going more than 65 miles per hour but less than 85 miles per hour are given a “Speeding” ticket.  Any cars going less than 65 are labeled “Safe” in the system.  

Fill in the blanks in this function so it returns the proper ticket type or label.
"""
print("###############Solution 2############")
def speeding_ticket(speed):
    if speed>=85:
        ticket = "Reckless Driving"
    elif speed > 65 and speed < 85:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket


print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding
print("\n")

#Question 3
"""
Fill in the blanks to complete the function.  The character translator function receives a single lowercase letter, then prints the numeric location of the letter in the English alphabet.  For example, “a” would return 1 and “b” would return 2. Currently, this function only supports the letters “a”, “b”, “c”, and “d” It returns "unknown" for all other letters or if the letter is uppercase.
"""
print("###############Solution 3############")
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position
    


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown
print("\n")

#Question 4
"""
Can you calculate the output of this code?
"""
print("###############Solution 4############")
def difference(x, y):
    z = x - y
    return z

print(difference(5, 3)) #Ouput = 2
print("\n")

#Question 5
"""
Fill in the blanks to complete the function. The “make_positive” function takes in a number and converts that number to its positive equivalent.  Complete the function to accomplish the following tasks:

    use an if statement to test if the number is negative;

    use a calculation inside the if statement to change the negative number to be positive;

    use a calculation in the else statement to return any positive “number” unchanged.
"""
print("###############Solution 5############")
def make_positive(number):
    if number < 0:
        result = number * -1 
    else:
        result = number
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5

