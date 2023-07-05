def open_or_senior(data):
    status = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            status.append("Senior")
        else:
            status.append("Open")
    return status
