def solution(s):
    lst = []
    for i in range(0, len(s), 2):
        el = s[i:i+2]
        if len(el) == 1:
            lst.append(el + '_')
        else:
            lst.append(el)
    return lst