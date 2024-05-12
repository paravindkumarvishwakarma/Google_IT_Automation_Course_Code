#----------Branching with if statement--------
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")
#This code will not have an output. 


def is_even(number):
    if number % 2 == 0:
        return True
    return False
#This code has no ouput

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

