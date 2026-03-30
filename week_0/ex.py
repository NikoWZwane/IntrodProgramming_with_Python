while True:
    try:
        x = int(input("What is x"))
    except ValueError:
        print(f"is not integer{x}")
    else:
        break
print(f"x is {x}")
