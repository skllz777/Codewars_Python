def is_anagram(test, original):
    a = ''.join(sorted((test).upper()))
    b = ''.join(sorted((original).upper()))
    return a == b

print(is_anagram("foefet", 'toffee'))

