#Taken from 4-1. Pizzas
pizzas = ["Pepperoni", "Deluxe Cheese", "Tuna Melt"]
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("\nI love pizza!")

friend_pizzas = pizzas[:]
pizzas.append("Meat Lover")
friend_pizzas.append("Sausage")

print("\nMy favourite pizas are:")
for pizza in pizzas:
    print(pizza + " Pizza")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza + " Pizza")
