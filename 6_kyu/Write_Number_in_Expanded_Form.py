def expanded_form(num):
    l = len(str(num)) - 1
    s = []
    for n in str(num):
        if n != '0':
            s.append(n + '0' * l)
        l -= 1
    return " + ".join(s)