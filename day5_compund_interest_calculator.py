# im building a calculater that finds your final amount using compound interest
Principle = 0  # initial deposit
rate = 0  # annual interest rate, expressed as a decimal
time = 0  # the number of years the money is invested
n = 0  # number of times interest is compounded per year

while Principle <= 0:
    Principle = float(input(("You're initial balance: ")))
    if Principle <= 0:
        print("Initial balance cannot be negative")
while rate <= 0:
    rate = float(input(("You're anual interest rate in decimal: ")))
    if rate <= 0:
        print("Anual interest cannot be negative")
while time <= 0:
    time = float(input("period of time you invested: "))
    if time <= 0:
        print("your invested year cannot be less than 0: ")

n = float(input("Enter number of time interest is compounded per year: "))

print(Principle)
print(rate)
print(time)
print(n)

A = round(Principle * pow((1 + rate/n), n * time), 3)
print(A)
