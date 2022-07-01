#
# Python:   3.10.5
#
# Author:   Mirwais Sarwary
# Date  :   June 30, 2022
#
# Purpose:  The Tech Academy - Python Course.
#           Demonstrating: python and databases 
#           Database Submission task:
#               create new table and tuple (fileList)
#               Add to table all fileList elements that meets specified requirements
#===================================================================================

#IMPORT SECTION:
import sqlite3


#1- creating a database only if not exists (file_name.db)
#hold our connection to the database with conn
conn = sqlite3.connect('test.db')
#with this open session do this
with conn:
    cur = conn.cursor()#cursor is used for operating on the database when commands are given
    #Creating new table fileList
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName TEXT)") #SQL statement
    conn.commit()#committing our changes
conn.close() #close the connection

#2- To add info into the created database
#establish and hold our connection to the database with conn
conn = sqlite3.connect('test.db')

#tuple of fileList:
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop that analyzes the tuple and finds those with .txt,
#then splits the fileList we want into a one-element tuples
#and finally adds it to the table (also prints it out in console)
with conn:
    cur = conn.cursor()
    for x in fileList:
        if x.endswith('.txt'):
            #adding data note...?'S are wildcards
            cur.execute("INSERT INTO tbl_fileList(col_fileName) VALUES (?)",(x,))
            conn.commit()#committing our changes
            print(x)
conn.close() #close the connection
