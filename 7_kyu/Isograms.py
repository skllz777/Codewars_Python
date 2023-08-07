def is_isogram(string):
    b = ''
    for chars in string.upper():
        if chars not in b:
            b += chars
    if len(string) == len(b):
        return True
    else:
        return False