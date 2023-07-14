def series_sum(n):
    ans = 0
    numbers = list(range(1, 3 * n, 3))
    for x in numbers:
        ans += 1 / x
    return '%.2f' % ans