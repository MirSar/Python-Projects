##import sqlite3

# get personal data from user
##firstName = input ("Enter your first name: ")
##lastName = input ("Enter your last name: ")
##age = int(input ("Enter your age: "))
##
##personData = (firstName, lastName, age)

# execute insert statement for supplied person data
##with sqlite3.connect ('test_database.db') as connection:
##    c = connection.cursor()
    # creating a table
##    c.execute("CREATE TABLE People (firstName TEXT, lastName TEXT, Age INT)")

    #Inserting data method 1
##    line = "INSERT INTO People VALUES ('"+ firstName +"','"+ lastName +"', " +str(age) +")"
##    c.execute(line)

    #Inserting data using parameterizing our statement
##    c.execute ("INSERT INTO People VALUES(?,?,?)", personData)
    
    # Updating data in Table
##    c.execute("UPDATE People SET Age=? WHERE firstName=? AND lastName=?",(46,'Mir','Sarwary'))

#######################################

import sqlite3

peopleValues = (('Ron','Obvious',42),('Luigi','Vercotti',43),('Arthur','Belling',28))

with sqlite3.connect ('test_database.db') as connection:
    c = connection.cursor()
    c.execute ("DROP TABLE IF EXISTS People")
    c.execute ("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany ("INSERT INTO People VALUES (?,?,?)", peopleValues)

    #select all first and last names from people over age 30
##    c.execute ("SELECT FirstName, LastName FROM People WHERE Age >30")
##    for row in c.fetchall():
##        print (row)

    # If we wanted to loop over our result rows one at a time instead of fetching them all at once
    c.execute ("SELECT FirstName, LastName FROM People WHERE Age >30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print (row)
        
