def queue_time(customers, n):
    t = [0] * n
    for x in customers:
        t[0] += x
        t.sort()
    return max(t)