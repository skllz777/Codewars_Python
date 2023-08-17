def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        principal = principal + (principal * interest) - (principal * interest * tax)
        count += 1
    return count