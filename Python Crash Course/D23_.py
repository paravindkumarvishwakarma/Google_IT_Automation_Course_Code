#Que-1) print the numbers 1 through 7.
print("print the numbers 1 through 7" + "\n")
number = 1 # Initialize the variable
while number <= 7: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 


#Que-2) Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.
print("Find and correct the error in the for loop below.  The loop should print every even number from 2 to 12.")
for number in range(2, 12, 2):
  print(number)

#Que-3) Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 #digits and 144 has 3 digits. 
#Tip: you can count the digits of a number by dividing it by 10 once per digit until there are no digits left.
print("Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. ")
def digits(n):
  count = 0
  if n == 0:
    count += 1
  while n>0: # Complete the while loop condition
      # Complete the body of the while loop. This should include 
      # performing a calculation and incrementing a variable in the
      # appropriate order.  
      n = n // 10
      count += 1
  return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

#Que-4) Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending order, #from the given "high" variable to the given "low" variable.  The range should make the loop run two times. Complete the range #sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:
#3, 2, 
#3, 2, 1
def sequence(low, high):
  # Outer loop to run twice (for two rows)
  for x in range(2): 
      # Inner loop to print numbers from high to low
      for y in range(high, low - 1, -1): 
          if y == low:
              # Don’t print a comma after the last item
              print(str(y)) 
          else:
              # Print a comma and a space between numbers
              print(str(y), end=", ") 

sequence(1, 3)
# Should print:
# 3, 2, 1
# 3, 2, 1





