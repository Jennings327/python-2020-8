'''
file = open('filetest.txt','w')
file.write('this is a test')
read_file = open('filetest.txt','r')
save = read_file.read()
print(save)
read_file.close()
'''

f = open('filetest.txt','w')
f.write('I am a student')
f.close()