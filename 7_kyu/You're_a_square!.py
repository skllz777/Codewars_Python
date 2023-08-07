import math


def is_square(n):
    if n < 0:
        return False
    else:
        if math.sqrt(n) ** 2 == n:
            return True
        else:
            return False
