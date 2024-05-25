#Common errors in for loops
"""for x in 25:
    print(x)"""    #this will produce an error


"""
for x in range(25):
    print(x)
"""                #this will make the error to go away


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")


