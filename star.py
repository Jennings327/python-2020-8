print('*',end='')
a = int(input('要幾行'))
for i in range(1,a+1):
    for n in range(a-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print('')