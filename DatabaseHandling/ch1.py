# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:15:44 2019

@author: harshvardhan
"""

import sqlite3
conn=sqlite3.connect("db_university")
c=conn.cursor()

c.execute("""CREATE TABLE stud(Student_Name TEXT,
                                  Student_Age INTEGER,
                                  Student_Roll_no INTEGER,
                                  Student_Branch TEXT)""")


c.execute("INSERT INTO stud VALUES ('Harsh','21', '1', 'CSE')")
c.execute("INSERT INTO stud VALUES ('Aditya','26', '2', '12thfail')")


c.execute("SELECT * FROM stud")
print ( c.fetchall() )
conn.commit()
conn.close()
