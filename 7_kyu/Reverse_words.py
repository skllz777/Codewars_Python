def reverse_words(text):
    text = text.split(' ')
    result = ''
    for word in text:
        result += " " + word[::-1]
    return result[1:]