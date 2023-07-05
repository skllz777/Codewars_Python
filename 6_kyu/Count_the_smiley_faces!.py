def array_diff(a, b):
    answer = []
    for num in a:
        if num not in b:
            answer.append(num)
    return answer