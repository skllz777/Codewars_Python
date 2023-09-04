def summa(arr, target):
    for ind1, num1 in enumerate(arr[:-1], start=0):
        for ind2, num2 in enumerate(arr[ind1 + 1:], start=ind1 + 1):
            if num1 + num2 == target:
                return [ind1, ind2]
