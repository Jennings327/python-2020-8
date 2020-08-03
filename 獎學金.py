x = input('輸一個數字')
x = int(x)
y = input('輸一個數字')
y = int(y)
if x>90 and y > 90: 
    print('有獎')
elif x or y == 100:
    print('有獎')
else:
    print('受罰')