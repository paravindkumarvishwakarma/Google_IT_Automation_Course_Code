#What is loops
#instruct your computer to continuously execute your code based on the value of a condition.

#Anotomy of a While Loop
#A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.  

#Example
x =   0 #Initialize
while x < 5: 
    print("Not there yet, x=" + str(x))
    x = x + 1 #Increment
print("x=" + str(x)) 
print("\n")

#Example 2
def attempts(n):
    x = 1 #Initialize
    while x <= n:
        print("Attempt " + str(x))
        x += 1 #Increament by 1
    print("Done")
print("\n")

#Example 3
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)
print("\n")

#Example 4
my_variable = 1
while my_variable < 10:
    print("Hello")
    my_variable += 1
print("\n")

#Example 5
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1
print("\n")

#Example 6
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
print("\n")


