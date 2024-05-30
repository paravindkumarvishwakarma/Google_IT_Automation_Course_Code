#Question 1:- What is recursion used for?
#Ans:- Recursion is used to call a function from inside the same function

#Question 2:-Which of these activities are good use cases for recursive programs? Check
#Ans: a) Going through a file system collecting information related to directories and files
     # b)Managing permission assigned to groups inside a company, when each group can contain both subgroups and users


#Question 3:- Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.
#Code
def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))    # Should be True
print(is_power_of(64, 4))   # Should be True
print(is_power_of(70, 10))  # Should be False


#Question 4:- Recursion is a process where a function calls itself one or more times with modified values to accomplish a task. This technique can be particularly effective when solving complex problems that can be broken down into smaller, simpler problems of the same type. In the provided code, the count_users function uses recursion to count the number of users that belong to a group within a company's system. It does this by iterating through each member of a group, and if a member is another group, it recursively calls count_users to count the users within that subgroup. However, there is a bug in the code! Can you spot the problem and fix it?
#Code
def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)
  return count


print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


#Question 5:- In the while loops practice quiz, you were asked to write a function to calculate the sum of all positive numbers between 1 and n. Rewrite the function using recursion instead of a while loop. Remember that when n is less than 1, the function should return 0 as the answer.
#Code
def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


