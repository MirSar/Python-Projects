#===================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:   DATABASES AND PYTHON CHALLENGE
"""
Complete these actions:
1. Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’
2. Populate your new table with the following values:
    1 Jean-Baptiste Zorg, Human, 122
    2 Korben Dallas, Meat Popsicle, 100
    3 Ak'not, Mangalore, -5
3. Update the Species of Korben Dallas to be Human.
4. Display the names and IQs of everyone in the table who is classified as Human.
"""

#===================================================================================
#================
# Import Section:
#================
import sqlite3

#=============
#Main Section:
#=============

# Create list of data to insert
tupleValues =(('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100),('Ak\'not', 'Mangalore', -5))
    
# Create a database table in RAM
with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    print ("connection established with dB in RAM")
    print("... ... ...")
    # Create table
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    print("Table named Roster is created")
    print("... ... ...")
    # Insert data from tuple
    c.executemany("INSERT INTO Roster VALUES(?,?,?)",tupleValues)
    print("Roster Table is populated")
    # Save (commit) the changes ... this is not really needed as it will automatically save upon closing
    connection.commit()
    print("Changes are committed")
    print("... ... ...")
    # Retrieving data from database
    c.execute("SELECT Name, Species, IQ FROM Roster")
    print("This is the original Roster")
    for row in c.fetchall():
        print(row)
    print("... ... ...")
    # Updating data entry
    c.execute("UPDATE Roster SET Species=? WHERE Name =? AND IQ =?",('Human','Korben Dallas',100))
    print("Correction made and one more human is added to the Roster")
    print("... ... ...")
    # Printing all humans from the table Roster
    print ("The following are names and IQs of everyone in the table who is classified as Human")
    c.execute("SELECT Name, IQ FROM Roster WHERE Species =='Human'")
    for row in c.fetchall():
        print(row)
        
#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first


if __name__ == "__main__":
    pass    #name of function or pass
    
#===================================================================================
#===================================================================================
