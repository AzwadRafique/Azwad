
while 1 == 1:
    message = input("> ")
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ";)": "😉",
        ":-x": "🤐",
        ":P": "😛",
        "-_-": "😑",
        "<3": "😍"so. D How are you Iamfine Thank you
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)
