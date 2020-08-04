a = int(input("全班有幾人?"))
list_score = []
name = []
for i in range(a):
    name_input = input('請輸入你的名字')
    score = int(input('請輸入成績:'))
    list_score.append(score)
    name.append(name_input)

sum_score = sum(list_score)
print('全班平均:',sum_score/a)

highest = 0
for n in range(a):
    if list_score[n] > highest:
        highest = list_score[n]
        high_name = name[n]
        
print(high_name,'最高分',highest)

lowest = 100
for k in range(a):
    if list_score[k] < lowest:
        lowest = list_score[k]
        low_name = name[k]
        

print(low_name,'最低分',lowest)

