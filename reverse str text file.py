'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''


f=open('dataset_24465_4 (4).txt','r')
s=[]
for line in f:
    line=line.rstrip()
    s.append(line)
s.reverse()
#cont="\n".join(s)
print()
print(s,"\n".join(s))
#z=[(s)for x in s]
#cont="\n".join(z)
#print(cont)



f.close()