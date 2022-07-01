#
# Python:   3.10.5
#
# Author:   Mirwais Sarwary
# Date  :   June 30, 2022
#
# Purpose:  The Tech Academy - Python Course.
#           Demonstrating: python and databases 
#           additional source: using sqlite3
#           Note:We didn't use functions,
#           however alway use functions for repeated tasks
#===================================================================================

###IMPORT SECTION###
import sqlite3

###MAIN SECTION###

#1- creating a database only if not exists (file_name.db)
#hold our connection to the database with conn
conn = sqlite3.connect('test.db')
#with this open session do this
with conn:
    cur = conn.cursor()#cursor is used for operating on the database when commands are given
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT, \
                col_lname TEXT, \
                col_email TEXT \
                )") #SQL statement
    conn.commit()#committing our changes
conn.close() #close the connection

#2- To add info into the created database
#establish and hold our connection to the database with conn
conn = sqlite3.connect('test.db')
#with this open session do this
with conn:
    cur = conn.cursor()#cursor is used for operating on the database when commands are given
    #adding data note...?'S are wildcards
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Amms','Sar','Amms@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Joy','Third','joyT@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Grace','Forever','graceF@gmail.com'))
    conn.commit()#committing our changes
conn.close() #close the connection

#3- Query our database for information
#establish and hold our connection to the database with conn
conn = sqlite3.connect('test.db')
#with this open session do this
with conn:
    cur = conn.cursor()#cursor is used for operating on the database when commands are given
    #Querying data
    cur.execute("SELECT col_fname,col_lname,col_email \
                    FROM tbl_persons \
                    WHERE col_fname = 'Amms'")
    #holding the information
    varPerson = cur.fetchall() #grabbing from a tuple
    for item in varPerson:
        #store as string
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    #print the data
    print(msg)
conn.close() #close the connection
