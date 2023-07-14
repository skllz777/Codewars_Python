def get_middle(s):
    a = len(s)
    b = len(s) // 2
    if a % 2 == 0:
        return s[b - 1] + s[b]
    else:
        return s[b]