def xo(s):
    x = []
    o = []
    for char in s.lower():
        if char == 'x':
            x.append(char)
        elif char == 'o':
            o.append(char)
    if len(x) == len(o):
        return True
    else:
        return False