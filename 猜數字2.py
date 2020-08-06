import random
min_num = 1
max_num = 1000
num = random.randint(min_num,max_num)

while True:
    print(min_num,max_num)
    ans=int(input('entry ans:'))
    if ans>max_num or ans<min_num:
        print('請輸入範圍',min_num,max_num)
    elif ans < num:
        min_num=ans
    elif ans > num:
        max_num=ans
    elif ans==num: 
        print('答對')
        break
    