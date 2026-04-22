print('*'*10)
print('YUMMY BANK')
print('*'*10)
c_password = 'python123'
number = 0
while number < 3:
    password = input('Enter password: ')
    if password == c_password:
        print('You are in')
        break
    else:
        print('Wrong password ole')
        number += 1
if number == 3:
    print('We have locked it ole')
