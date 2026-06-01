import emoji
message = input("Input: ")
message = emoji.emojize(f"{message}", language="alias")
print(message)