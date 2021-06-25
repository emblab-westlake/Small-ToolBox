# -*- coding: utf-8 -*-
'''
Author: zhangguoqing
Date: 2021-06-25 21:20:32
LastEditTime: 2021-06-25 21:31:17
'''

fr=open('test2.fasta', 'r')
fw=open('out.fasta', 'w')
seq={}
for line in fr:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
#        name=line.split()[0]    #以空格为分隔符，并取序列为0的项。
        name=line.replace('\n', '')    #以空格为分隔符，并取序列为0的项。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()                           

for i in seq.keys():
    fw.write(i)
    fw.write('\n')
    fw.write(seq[i])
    fw.write('\n')
fw.close()


'''
如果要选择指定的ID序列，启用一下命令

for i in seq.keys():
    if i.startswith('>chr1|hos107.1'): #该行命令的添加，可以输出指定ID的序列。
        fw.write(i)
        fw.write('\n')
        fw.write(seq[i])
        fw.write('\n')
fr.close()
'''