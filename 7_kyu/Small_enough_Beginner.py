def small_enough(array, limit):
    array1 = []
    for number in array:
        if number <= limit:
            array1.append(number)
    if len(array1) == len(array):
        return True
    else:
        return False