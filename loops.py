muffins = 10
cupcakes = 10

while True:
    order = input("What would you like to buy? ")

    if order == "0":
        break
    elif order == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif order == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")

print(f"muffins: {muffins} cupcakes: {cupcakes}")
