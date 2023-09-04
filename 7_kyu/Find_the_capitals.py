def capitals(word):
    ind_lst = []
    for index, char in enumerate(word):
        if char.isupper():
            ind_lst.append(index)
    return ind_lst