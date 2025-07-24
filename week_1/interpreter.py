
expression = input("Enter an arithmetic expression: ")
num_1, maths_operator, num_2 = expression.split()
x = int(num_1)
z = int(num_2)
if maths_operator == "+":
    result = x + z
elif maths_operator == "-":
    result = x - z
elif maths_operator == "*":
    result = x * z
elif maths_operator == "/":
    result = x / z
else:
    result = None

if result is not None:
    print(f"{result:.1f}")
else:
    print("Invalid operator. Please use +, -, *, or /.")
