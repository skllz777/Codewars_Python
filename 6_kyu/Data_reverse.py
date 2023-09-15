def data_reverse(data):
    d = []
    for i in range(0, len(data), 8):
        d.append(data[i:i + 8])
    return list(sum(d[::-1], []))