def remove_url_anchor(url):
    ans = ''
    for char in url:
        if char != "#":
            ans += char
        if char == '#':
            break
    return ans