food_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.0

while True:
    order = input("Item: ")
    
    if order in food_menu:
        total += food_menu[order]
        print(f"Total R{food_menu[order]:.2f}")
        print(f"Total: R{total:.2f}")
        
    elif order == "c":
        print(f"Final Total: R{total:.2f}")
        break
        
    else:
        print("Item not found.")
