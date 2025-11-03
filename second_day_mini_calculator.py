# input() - function that prompts the user to input data and
#           returns the entered data as a string

name = input("Hello my name is Anujin, What is your name? ")
print(f"Nice you meet you {name} ")


# I'll try mini calculator here

a = float(input("Please enter your number (a): "))
b = float(input("Please enter your number (b): "))
operator = input("Please choose your operating tool(*,+,-,/): ")


if operator == "*":
    result = a * b
    print(round(result, 3))
elif operator == "+":
    result = a + b
    print(round(result, 3))
elif operator == "-":
    result = a - b
    print(round(result, 3))
elif operator == "/":
    result = a / b
    print(round(result, 3))

