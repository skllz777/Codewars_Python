def gimme(a):
    if a[2] < a[0] < a[1] or a[1] < a[0] < a[2]:
        return 0
    if a[2] < a[1] < a[0] or a[0] < a[1] < a[2]:
        return 1
    if a[0] < a[2] < a[1] or a[1] < a[2] < a[0]:
        return 2