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


