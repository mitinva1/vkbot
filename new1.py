#!/usr/bin/python3
# -*- coding: utf-8 -*-


f2 = open("answer_databse.txt")
def insert(s1,s2):
    import sqlite3
    conn = sqlite3.connect('answerdb2.sqlite3')
    c = conn.cursor()
    c.execute("""insert into answers values ('%s','%s')"""%(s1,s2))
    conn.commit()
    c.close()
z=[]
f2 = open("answer_databse.txt")
for x in f2:
	z.append(x[:-2])#аполняем перый список

zz=[]
for x in z:
	for x1 in x:
	    if x1!='\\':
	        sl1 += x1
	    else:
	        zz.append(sl1)
	        sl1=''

for x in range(0, len(zz), 2):
	insert(zz[x],zz[x+1])
