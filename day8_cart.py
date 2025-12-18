# Today i'm going to build a list of your cart products
items = []
prices = []

print(" \n Hello Good morning, let's build your cart \n")

while True:
    item = input("what would you like? ")
    if item == "q":
        break
    else:
        price = float(input(f"This {item} :$ "))
        print(f"✅successfully added {item} for {price:.2f}")
        items.append(item)
        prices.append(price)

print("-" * 40)
print(" Your reciept")
print("-" * 40)

for item in items:
    print(item)

total = 0

for price in prices:
    total += price
print(f"Your total comes to {total:.2f}")
