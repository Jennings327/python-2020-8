import random
num = random.randint(1,10)

ans = int(input('1~10:'))
while num!=ans:
    print('猜錯了')
    ans = int(input('1~10:'))
    
    if num==ans:
        print('猜對了')
        break
    
        