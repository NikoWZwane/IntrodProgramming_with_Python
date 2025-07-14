def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":()", "🙁")

    return text
sentence = "Hello :) and goodbye :("
convert_sentence = convert(sentence)
print(convert_sentence)