def odd_or_even(arr):
    if len(arr) > 0:
        if sum(arr) % 2 == 0:
            return "even"
        else:
            return 'odd'
    if len(arr) == 0:
        return 'array with a zero'
