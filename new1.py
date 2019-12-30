#!/usr/bin/python3
# -*- coding: utf-8 -*-


z = []

word = ''
with open("answer_databse.txt") as file_handler:
    for line in file_handler:
        z.append(line)

rec = 0
d=''
z1 = []
for lines in z:
    for x in lines:
        if x != '\\' and x !='\n' and x != '2':
            d = d+x
        else:
            if len(d)>0:
                z1.append(d)
            d = ''
