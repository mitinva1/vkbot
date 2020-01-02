#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sqlite3
conn = sqlite3.connect('answerdb1.sqlite3')
c = conn.cursor()
answer = '2'
t = (answer,)
c.execute('select answer from answers where question=?', t)
answer = c.fetchall()[0]
answer = answer[0]
