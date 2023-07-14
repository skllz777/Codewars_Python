def number(bus_stops):
    ans = 0
    for element in bus_stops:
        ans += element[0] - element[1]
    return ans
