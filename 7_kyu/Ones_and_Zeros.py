def binary_array_to_number(arr):
    binary = ''
    for numbers in arr:
        binary += str(numbers)
    return int(binary, 2)