def get_sum(a, b):
    x = 0
    if a == b:
        return a
    small, big = sorted([a, b])
    return sum([i for i in range(small, big + 1)])