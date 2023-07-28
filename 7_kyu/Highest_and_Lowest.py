def high_and_low(numbers):
    p = numbers.split()
    ans = []
    for s in p:
        ans.append(int(s))
    result = "{} {}".format(max(ans), min(ans))
    return result