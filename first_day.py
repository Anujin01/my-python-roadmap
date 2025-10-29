# variables is a container for a value that has
# 4 basic datatypes: string, integer, float and boolean.

# string example
first_name = "Anujin"
print(f"Hello, my name is {first_name}")

# integers
age = 20
print(f"I'm {age} years old. ")

# float
price = 10.09
print(f"this paper is ${price}")

# boolean
school = True
print(f"Do you go to school: {school}")
if school:
    print("you go to school everyday.")
else:
    print(" you dont go to school")

# to get to know what datatype is your variable, we use type function
# we can convert variable from one data type to another
print(type(age))
print(type(school))
school = int(school)
print(type(school))
