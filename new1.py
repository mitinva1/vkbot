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
