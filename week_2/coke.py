total_due = 50
print("Amount due: 50")

while total_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        total_due = total_due - coin
        if total_due > 0:
            print(f"Amount due: {total_due}")
        elif total_due <= 0:
            print(f"Change owed: {abs(total_due)}")
    else:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")

