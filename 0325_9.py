def chgPriv(text):
    text = text.replace(text[len(text)-4:], "####")
    return text


print(chgPriv("park 010-9999-9988"))
