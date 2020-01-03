#!/usr/bin/python3
# -*- coding: utf-8 -*-

def answer_db(question):
    import sqlite3
    conn = sqlite3.connect('answerdb2.sqlite3')
    c = conn.cursor()
    answer = question
    t = (answer,)
    c.execute('select answer from answers where question=?', t)
    answer = c.fetchall()[0]
    answer = answer[0]
    return answer