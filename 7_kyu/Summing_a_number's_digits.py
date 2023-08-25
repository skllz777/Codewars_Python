def sum_digits(number):
    summa = 0
    if number < 0:
        number *= -1
    while number > 0:
        summa += number % 10
        number = number // 10
    return summa
