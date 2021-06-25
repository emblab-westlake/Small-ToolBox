# -*- coding: utf-8 -*-
'''
Author: zhangguoqing
Date: 2021-06-25 22:02:33
LastEditTime: 2021-06-25 22:14:06
'''
fr=open('protein_fasta_protein_homolog_model.fasta', 'r')
fw=open('card.fasta', 'w')
seq={}
for line in fr:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name_temp="|".join((line.split('|')[0],line.split('|')[1]))  #以空格为分隔符，并取序列为0的项。
        print(name_temp)
        name=name_temp.replace('>gb', '>CARD_gb')    #以空格为分隔符，并取序列为0的项。
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