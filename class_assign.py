#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#           
# Assignment:   Create a parent and 2 child classes
#           
#===================================================================================
#Classes Iheritance

#Parent Class = User
class User:
    #class attributes
    name = "NoName"
    email = ""
    password = "defaultPass123"
    accountID = 0
    
    #class methods -login
    def login(self):
        entry_email = input ("Enter your email: ")
        entry_password = input ("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print ("Welcome back, {} !".format(self.name))
        else:
            print ("You are not authorized for this page.")
    
    #class method - new class by initialization
    def __init__(self, name, email, password, accountID):
        self.name = name
        self.email = email
        self.password = password
        self.accountID = accountID

#Creating child classes:
class Employee (User):
    #adding additonal attributes
    base_pay = 80.00
    department = 'Engineering'

class Customer (User):
    #adding additonal attributes
    mailing_address = ""
    mailing_list = True



#Creating an isntance of the User class

def start():
    #new objects being created in a single line of code
    New_User = User('Ronin', 'Ro@gmail.com','Ropass123',1)
    New_User2 = Employee ('Mir','MS@gmail.com','MSpass123',2)
    New_User3 = Customer('Amms', 'amms@gmail.com','ammspass123',3)
    #printing the results
    print (New_User.name,'\n',New_User.email,'\n')
    print (New_User2.name,'\n',New_User2.department,'\n')
    print ("{} is in the mailing list: {}".format(New_User3.name,New_User3.mailing_list))



#program flow control
if __name__ == "__main__": #looks at this first to see which script to run first
    start()
