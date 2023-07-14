def disemvowel(string_):
    x = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ''
    for char in string_:
        if char not in x:
            ans += char
    return ans
