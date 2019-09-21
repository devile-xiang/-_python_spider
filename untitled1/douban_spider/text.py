import codecs

list = [[1,2],[3,4]]

s = u'亚像素精度：\r\n'  #u表示读取中文，\r\n为换行符
f = codecs.open("dome1.py.txt",'w','utf-8')

f.write(s)
#f.write(str(list))
for i in list:
    f.write(str(i)+'\r\n')  #\r\n为换行符

f.close()