
try:
    num , den = (input("Fraction: ").split("/"))
    num , den = int(num), int(den) 
    total = 100 * num // den 
    print(f"{total}%")
except ValueError:
    print(input("fraction").split("/"))
except ZeroDivisionError:
    print("cant divide by zero")


