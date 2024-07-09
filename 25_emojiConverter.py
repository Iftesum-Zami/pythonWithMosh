massage = input("> ")
words = massage.split(" ")  # .split() splits the words in sentence and return them in a list by default

emojis = {
    ":)": "😊",
    ":(": "😞"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
