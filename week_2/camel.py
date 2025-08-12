camel_name = input("Enter name of a variable in camel case: ")

snake_name = ""
for char in camel_name:
    if char.isupper():
        snake_name += "_" + char.lower()
    else:
        snake_name += char

print("snake_case:", snake_name)
