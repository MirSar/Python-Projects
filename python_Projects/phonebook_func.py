#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Assignment:   phonebook application
#               phonebook_func module/file contains all of
#               the function codes
#
# Date:         7/8/2022
#
#===================================================================================
#----------------------------------------------------------
# Import Section:

import os
from tkinter import *
from tkinter import messagebox #this is needed to import messagebox
import tkinter as tk
import sqlite3
import phonenumbers #For phone number Validation

#custome modules
import phonebook_main
import phonebook_gui

#-----------------------------------------------------------
# Main Section:

def center_window(self,w,h): #pass in the tkinter frame(master) reference and the w and h
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth() #gets users screen w and stores it in our var
    screen_height = self.master.winfo_screenheight() #gets users screen h and stores it in our var
    #calculate x and y coord to paint the app centered on the user's screen
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X'to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel('Exit Program','Okay to exit application?'):
        # This closes app
        self.master.destroy()
        os._exit(0) # closes unused widgets, avoid memory leak

#****************************************
def create_db(self):
    conn = sqlite3.connect('phonebook.db')#creates database and connects
    with conn:
        cur = conn.cursor() #cursor is needed to send in commands to sql
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # Commit() to save changes and close the dB connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John','Doe','John Doe','+1-111-111-1111','jdoe@email.com') # tuple dummy-data so dB has values
    conn = sqlite3.connect('phonebook.db')#db is created so this will only connect
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur) #temp passing cur to our function count_records;will return cur and count back 
        if count <1: # only for the first run! if no info, count=0, then do:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email)VALUES(?,?,?,?,?)""",(data[0],data[1],data[2],data[3],data[4]))
            conn.commit()
    conn.close()

def count_records(cur):
    count ="" #creates an empty variable, count
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""") #needed the cur to be passed here
    count = cur.fetchone()[0] #code to extract the count. calls the first item in the tuple
    return cur,count #returns back cur control and count value

# Select item in ListBox
def onSelect(self,event): #self give it access to this class, event gives user information
    #calling the event is the self.lstList1 widget
    varList = event.widget #event.widget = whatever that is triggering the event
    select = varList.curselection()[0]#catch the first index of the tuple
    value = varList.get(select)# get the text of the index passed to here
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""",[value])
        varBody = cursor.fetchall()#accessing information outside of SQLite3 db
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END) #delete the txt box from begining to end (all of it)
            self.txt_fname.insert(0,data[0]) #insert the new info
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # This will ensure that the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combines our normalized names into a fullname
    print("var_fullname: {}".format(var_fullname)) #!!Just for development purpose!!
    var_email = self.txt_email.get().strip()

    #Phone number with + for country code - needed for validation
    norm_phone = self.txt_phone.get().strip()
    countryCode= '+'
    var_phone = countryCode + norm_phone
    
    if (len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and (len(var_email)>0):#enforce data entry
        #validating the phone number
        parsePhoneNo = phonenumbers.parse(var_phone)
        isPhoneNoValid= phonenumbers.is_valid_number(parsePhoneNo)
        if isPhoneNoValid == False: # Error message if the phone is not valid
            messagebox.showerror("Invalid Phone Number!","Please enter a valid phone number!\n (country code)(area code)(phone number)")
            print(isPhoneNoValid)
        elif not "@" or not "." in var_email: #semiValidation of email 
            messagebox.showerror("Invalid Email!","Please enter a valid email!")
        else: 
            conn = sqlite3.connect('phonebook.db')
            with conn:
                cursor = conn.cursor()
                # check the db for existance of the fullname, if so we will alert user and disregard request
                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
                count = cursor.fetchone()[0]
                chkName = count
                if chkName == 0: # If this is 0 then there is no existance of the fullname and we can add new data
                    print("chkName: {}".format(chkName))#!!!for development use only!!!
                    cursor.execute("""INSERT INTO tbl_phonebook(col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                    self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                    onClear(self) # call the function to clear all of the textboxes
                else:
                    messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                    onClear(self)
            conn.commit()
            conn.close()
    else:
        messagebox.showerror("Missing Text Error!","Please enter correct data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # Check count to ensure that this is not the last record in
        #the dB ... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""") #count all rows
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All info associated with, ({}) \nwill be permenantly deleted.".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                    onDeleted(self) # Call the func to clear all of the textboxes and the selected index of listbox
                    conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and cannot be deleted at this time".format(var_select))
    conn.close()

def onDeleted(self): # Note this is onDeleted past-tense
    # Clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    try: # Deletes the username from the listbox (once it is deleted from dB)
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # Clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i=0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i += 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # Index of the list selection
        var_value = self.lstList1.get(var_select) # List selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be allowed to update the changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
     
    var_email = self.txt_email.get().strip() # Normalize the data to maintain dB integrity
    #Phone number with + for country code - needed for validation
    norm_phone = self.txt_phone.get().strip()
    countryCode= '+'
    var_phone = countryCode + norm_phone
    
    if (len(var_phone) > 0) and (len(var_email) > 0): # Ensure that there is data present
        #validating the phone number
        parsePhoneNo = phonenumbers.parse(var_phone)
        isPhoneNoValid= phonenumbers.is_valid_number(parsePhoneNo)
        if isPhoneNoValid == False: # Error message if the phone is not valid
            messagebox.showerror("Invalid Phone Number!","Please enter a valid phone number!\n (country code)(area code)(phone number)")
            print(isPhoneNoValid)
        #semiValidation of email
        elif not "@" or not "." in var_email:  
            messagebox.showerror("Invalid Email!","Please enter a valid email!")

        else:    
            conn = sqlite3.connect('phonebook.db')
            with conn:
                cur = conn.cursor()
                # Count records to see if the user's changes are already in
                #the dB...meaning, there are no changes to update.
                cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
                count = cur.fetchone()[0] #count for the phone
                print (count) #!!!Dev purpose only!!!
                cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
                count2 = cur.fetchone()[0] #count for the email
                print(count2) #!!!Dev purpose only!!!
                if count == 0 or count2 == 0: # If proposed changes are not already in the database, then proceed
                    response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}).\n\nProceed with the update request?".format(var_phone,var_email,var_value))
                    print(response) #!!!Dev purpose only!!!
                    if response:
                        with conn:
                            cursor = conn.cursor()
                            cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                            onClear(self)
                            conn.commit()
                    else:
                        messagebox.showinfo("Cancel request","No changes have been made to ({})".format(var_value))
                else:
                    messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name.\n\nYour update has been cancelled".format(var_phone,var_email))
                onClear(self)
            conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list.\nThen edit the phone or email information.")
    onClear(self)
                                                                                                                                 
#-----------------------------------------------------------
#program flow control
if __name__ == "__main__":
    pass
