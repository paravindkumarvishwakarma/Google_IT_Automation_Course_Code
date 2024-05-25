#Question 1: How are while loops and for loops different in Python?
#Ans: while loops iterate while a condition is true; for loops iterate through a sequence of elements

#Question 2: Which option would fix this for loop to print the numbers 12,18,24,30,36?
"""
for n in range(6,18,3):
    print(n*2)
"""
#Ans: 
for n in range(6,18+1,3):
    print(n*2)

#Question 3: Which for loop will print all even numbers from 0 to 18?
#Ans
for n in range(19):
    if n % 2 == 0:
        print(n)


#Question 4: Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10
#Ans:
        for x in range(1,11):
            print(x**3)

#Question 5: Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7
#Ans: 
for x in range(7,101,7):
    print(x)

#Question 6: Which of these options would output just the vowels from the following strings? Select all that
#Ans
print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])

#Question 7: Which of these statement is true about slicing strings?
#Ans: The slice() method can be used to slice a string