password = input('Please enter your password: ')
dig = False
low = False
up = False
for char in password:
    if char.isdigit():
        dig = True
    elif char.islower():
        low = True
    elif char.isupper():
        up = True
reliability = 0
if dig:
    reliability += 1
if up:
    reliability += 1
if low:
    reliability += 1
if len(password) >= 8:
    if reliability == 3:
        print("Your password is reliable!")
    if reliability == 2:
        print('Your password is good!')
    if reliability == 1:
        print('Your password is weak!')
else:
    print('Your password is invalid!')