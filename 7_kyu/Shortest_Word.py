def find_short(s):
    result = list(map(len, s.split()))
    return min(result)