# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:59:42 2019

@author: harshvardhan
"""

import mysql.connector
conn = mysql.connector.connect ( user='root', password='root', host='localhost')
c=conn.cursor()
c.execute("DROP DATABASE practise;")
c.execute("CREATE DATABASE practise;")
c.execute("USE practise;")
c.execute("""CREATE TABLE test(id INTEGER,name TEXT)""")

c.execute("INSERT INTO test VALUES (01,'Harsh')")
c.execute("INSERT INTO test VALUES (02,'Aditya')")
c.execute("SELECT * FROM test")
print(c.fetchall())
conn.commit()
conn.close()