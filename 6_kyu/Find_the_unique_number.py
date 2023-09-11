def find_uniq(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num