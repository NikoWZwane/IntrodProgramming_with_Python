from collections import Counter

enter_items = []  # list to store items

while True:
    item = input("Enter item (or 'c' to stop): ")
    
    if item == "c":
        break
    
    enter_items.append(item)   # add item to list

# Count items
counted = Counter(enter_items)

# Print counts nicely
for item, count in counted.items():
    print(f"{item} x{count}")
