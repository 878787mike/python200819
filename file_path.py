import os.path
file=open('y.txt','w')
if os.path.isfile('y.txt'):
    print('it is here')
    file=open('y.txt','a')
    file.write('這檔案94here')
else:
    print('not here')
    file.open('y.txt','w')
    file.write('這是新增的檔案')