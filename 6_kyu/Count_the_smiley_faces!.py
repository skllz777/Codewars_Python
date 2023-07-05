def count_smileys(arr):
    answer = []
    for char in arr:
        if len(char) == 2 and char[0] in [':', ";"] and char[1] in [')', 'D']:
            answer.append(char)
        elif len(char) > 2 and char[0] in [':', ";"] and char[1] in ['-', '~'] and char[2] in [')', 'D']:
            answer.append(char)
    return len(answer)