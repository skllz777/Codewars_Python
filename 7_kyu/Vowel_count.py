def get_count(sentence):
    count = []
    for char in sentence:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count.append(char)
    return len(count)