def order(sentence):
    digits = []
    answer = ''
    for char in sentence:
        if char.isdigit():
            digits.append(char)
    for digit in sorted(digits):
        for words in sentence.split():
            if digit in words:
                answer += words
                answer += ' '
    return answer[:-1]