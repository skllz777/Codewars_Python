def number(lines):
    answer = []
    for i in range(0, len(lines)):
        element = str(i + 1) + ": " + lines[i]
        answer.append(element)
    return answer