#file = open('filetest.txt','w')

#file.write('this is a test')

read_file = open('filetest.txt','r')

save = read_file.read()

print(save)

read_file.close()