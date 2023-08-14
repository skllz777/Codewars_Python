def to_jaden_case(string):
    string = string.split()
    ans = ''
    for word in string:
        ans += word.capitalize()
        ans += ' '
    return ans[:-1]