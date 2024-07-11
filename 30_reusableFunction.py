def emoji_converter(message):  # here, message is a local variable, not global. Only works inside function
    words = message.split(" ")  # .split() splits the words in sentence and return them in a list by default

    emojis = {
        ":)": "😊",
        ":(": "😞"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


userMessage = input("> ")
result = emoji_converter(userMessage)
print(result)
