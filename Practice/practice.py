num = 70304
s = []
i = len(str(num)) -1
print(i)
for n in str(num):
    if n != "0":
        s.append(n + "0" * i)
    i -= 1
print(s)
g = '7' + '0' * 4
print(g)