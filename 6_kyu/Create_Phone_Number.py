def create_phone_number(n):
    phone = ''
    for num in n:
        phone += str(num)
    return f'({phone[0:3]}) {phone[3:6]}-{phone[6::]}'