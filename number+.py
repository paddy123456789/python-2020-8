import random
num = random.randint(1,10)

while True:
    a=int(input('1~10:'))
    if a==num:
        print('猜對了!')
        break
    else:
        print('猜錯了!')
        