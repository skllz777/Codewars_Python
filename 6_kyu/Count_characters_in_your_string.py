def count(s):
    ans = dict()
    for char in s:
        ans[char] = ans.get(char, 0) + 1
    return ans