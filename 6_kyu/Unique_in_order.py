def unique_in_order(sequence):
    answer = []
    prev_char = ''
    for char in sequence:
        if char != prev_char:
            answer.append(char)
            prev_char = char
    return answer