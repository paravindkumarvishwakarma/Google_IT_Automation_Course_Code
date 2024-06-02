#What is recursion?
"""The repeated application of the same procedure to a smaller problem
   Recursion lets us tackle complex problem by reducing the problem to a similar one
   In programming, recursion is a way of doing a repetitive task by having a function call itself.
"""

"""def factorial(n):
    if n<2:
        return 1
    return n * factorial(n-1)"""

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)


