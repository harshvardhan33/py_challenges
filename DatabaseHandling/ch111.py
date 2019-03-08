# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:34:24 2019

@author: harshvardhan
"""



import mysql.connector
conn = mysql.connector.connect ( user='root', password='root', host='localhost')
c = conn.cursor()
c.execute("CREATE DATABASE student;")
c.execute("USE student;")
c.execute("""CREATE TABLE stud(Student_Name TEXT,
                                  Student_Age INTEGER,
                                  Student_Roll_no INTEGER,
                                  Student_Branch TEXT)""")


c.execute("INSERT INTO stud VALUES ('Harsh','21', '1', 'CSE')")
c.execute("INSERT INTO stud VALUES ('Aditya','26', '2', '12thfail')")
conn.commit()
conn.close()
