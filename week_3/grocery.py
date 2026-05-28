items = {}
try:
    while True:
        item = input()
        if item in items:
            items[item]+=1
        else:
            items[item] = 1

except EOFError:
    print()

for item, count, in items.items():
    print(f"{count} {item}".upper())