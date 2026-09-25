SLICES_PER_PIZZA = 8

print("Pizza Calculator - Family of 4")
print("Each pizza has", SLICES_PER_PIZZA, "slices.")
print()

person1 = int(input("How many slices will Person 1 eat? "))
person2 = int(input("How many slices will Person 2 eat? "))
person3 = int(input("How many slices will Person 3 eat? "))
person4 = int(input("How many slices will Person 4 eat? "))

total_slices_needed = person1 + person2 + person3 + person4

whole_pizzas = total_slices_needed // SLICES_PER_PIZZA
remainder = total_slices_needed % SLICES_PER_PIZZA

if remainder > 0:
    whole_pizzas = whole_pizzas + 1

leftover_slices = (whole_pizzas * SLICES_PER_PIZZA) - total_slices_needed

print()
print("Total slices needed:", total_slices_needed)
print("Pizzas to order:", whole_pizzas)
print("Leftover slices:", leftover_slices)
