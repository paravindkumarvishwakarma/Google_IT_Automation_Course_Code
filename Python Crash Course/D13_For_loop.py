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


