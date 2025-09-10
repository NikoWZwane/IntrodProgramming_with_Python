lng_text = input("Enter text: ")
words_to_remove = list("AEIOUaeiou")
new_text = []
for i in lng_text:
    if i not in words_to_remove:
        new_text.append(i)
print("".join(new_text))