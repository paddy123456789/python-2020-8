import random
a=1
b=100
num = random.randint(a,b)

while True:
    print('目前的範圍%d-%d'%(a,b))
    ans = int(input('輸入數字:'))
    if ans<a or ans>b:
        print('請重新輸入數字')
    elif ans>num:
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        print('得分')
        break
   
        