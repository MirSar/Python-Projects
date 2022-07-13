#==================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      Student Tracker application: using Tkinter GUI

# Assignment:   The Tech Academy - Python Course
#               The tkinter package (“Tk interface”) is the
#               standard Python interface to the Tcl/Tk GUI toolkit.

#               stuTracker_func = functions module

#               Contains: all of the function/methods

#===================================================================================
# Import Section:
#================

import os

# version Tcl/Tk 8.6
from tkinter import *

# This is needed to import messagebox
from tkinter import messagebox

import tkinter as tk
import sqlite3

# For phone number Validation
import phonenumbers 

# Custome modules
import stuTracker_main
import stuTracker_gui

#===================================================================================
# Main Section:
#==============

# Passing in the tkinter frame, master, reference
# and the w and h of our app window
# Called by stuTracker_main
def center_window(self,w,h):
    
    # Getting the user's screen width and height
    # and storing it in our variables
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    
    # Calculating x and y coord to paint the app such that
    # the app is centered on the user's screen
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

#---------------

# When the user's clicks on the windows upper-right 'X'
# this method asks if they want to close the window.
# Called by stuTracker_main
def ask_quit(self):
    if messagebox.askokcancel("Exit Program","Listen up, here is the DEAL\nYou click that OK btn\nand I'll close the window."):
        # This closes app
        self.master.destroy()
        # closes unused widgets, avoid memory leak
        os._exit(0)
        
#---------------

# Called by stuTracker_gui
def create_db(self):

    # First time it creates database and establishes connection
    conn = sqlite3.connect('stuTracker.db')
    with conn:
        
        # Cursor is needed to send in commands to sqlite3
        cur = conn.cursor()

        # Create a Table in the database
        cur.execute("CREATE TABLE if not exists tbl_stuTracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_curCourse TEXT \
            );")
        
        # Commit() to save changes and close the dB connection
        conn.commit()
    conn.close()

    # Setting up the newly created database
    first_run(self)

#---------------

# First run setup of the database
# Called by create_db()
def first_run(self):

    # Initial setup dummy tuple data
    data = ('Bruce','Wayne','Bruce Wayne','+1-111-111-1111','bats@email.com','computer science') 

    # dB exists so this will only connect
    conn = sqlite3.connect('stuTracker.db')
    with conn:
        cur = conn.cursor()

        # Temp passing cur to our internal method count_records()
        # checking if any records exist in the dB 
        cur,count = count_records(cur)

        # If the dB is empty, then insert dummy data
        if count < 1: 
            cur.execute("""INSERT INTO tbl_stuTracker \
                        (col_fname,\
                        col_lname,\
                        col_fullname,\
                        col_phone,\
                        col_email, \
                        col_curCourse)VALUES(?,?,?,?,?,?)""",\
                        (data[0],data[1],data[2],data[3],data[4],data[5]))

            # Commit change
            conn.commit()

    # Close connection
    conn.close()

#---------------

# Called by first_run()    
def count_records(cur):
    
    # Creates an empty variable, count
    count ="" 

    # Sqlite3 inquery ...count all rows of table
    cur.execute("""SELECT COUNT(*) FROM tbl_stuTracker""") 

    # Checking to see if there are any records in the table
    # needs to only call the first item in the tuple
    count = cur.fetchone()[0]

    # Returns back cur control and count value
    return cur,count 

#---------------

# Triggered by user's selection of an item in Listbox
# event gives user information(listbox clicks)
# Called by stuTracker_gui
def onSelect(self,event):
    
    # called by self.lstList1 widget
    # event.widget = 'whatever that is triggering the event'
    varList = event.widget 

    # catches the first index of the tuple
    select = varList.curselection()[0]

    # gets the text of the index passed to here
    value = varList.get(select)
    conn = sqlite3.connect('stuTracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_curCourse \
                            FROM tbl_stuTracker \
                            WHERE col_fullname = (?)""",[value])
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
            self.txt_curCourse.delete(0,END)
            self.txt_curCourse.insert(0,data[4])

#---------------
            
def addToList(self):
    
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    
    # normalize the data to keep it consistent in the database

    # This will remove any blank spaces before and after the user's entry
    var_fname = var_fname.strip() 
    var_lname = var_lname.strip()

    # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title() 
    var_lname = var_lname.title()

    # combines our normalized names into a fullname
    var_fullname = ("{} {}".format(var_fname,var_lname)) 

    #!!check point. development purpose!!
    print("var_fullname: {}".format(var_fullname)) 

    var_email = self.txt_email.get().strip()
    var_curCourse = self.txt_curCourse.get().strip()

    #Phone number with + for country code - needed for validation
    norm_phone = self.txt_phone.get().strip()
    countryCode= '+'
    var_phone = countryCode + norm_phone

    #Verifying data entry
    if (len(var_fname)>0) and (len(var_lname)>0) and (len(var_phone)>0) and (len(var_email)>0) and (len(var_curCourse) > 0) :

        #validating the phone number                                                                               
        parsePhoneNo = phonenumbers.parse(var_phone)
        isPhoneNoValid= phonenumbers.is_valid_number(parsePhoneNo)

        # Error message if the phone is not valid                                                                                          
        if isPhoneNoValid == False: 
            messagebox.showerror("Invalid Phone Number!","Please enter a valid phone number!\nInclude the following:\n (country code)-(area code)-(phone number)")
            print(isPhoneNoValid)

        #verify email layout                                                                                            
        elif not "@" or not "." in var_email: 
            messagebox.showerror("Invalid Email!","The computer said \"Noooooo\"\nCome on, enter a valid email!")

        else: 
            conn = sqlite3.connect('stuTracker.db')
            with conn:
                cursor = conn.cursor()
                # check the db for existance of the fullname, if so we will alert user and disregard request
                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_stuTracker\
                                WHERE col_fullname = '{}'""".format(var_fullname))
                count = cursor.fetchone()[0]
                chkName = count

                # If this is 0 then there is no existance of the fullname and we can add new data
                if chkName == 0:

                    #!!!for development use only!!!
                    print("chkName: {}".format(chkName))
                    
                    cursor.execute("""INSERT INTO tbl_stuTracker\
                                    (col_fname,col_lname,col_fullname,col_phone,col_email,col_curCourse)\
                                    VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_curCourse))

                    # update listbox with the new fullname  
                    self.lstList1.insert(END, var_fullname)
                    # call the function to clear all of the textboxes
                    onClear(self)
                    
                else:
                    messagebox.showerror("Name Error","\"{}\" already exists in the database!\n \
                                        Please choose a different name".format(var_fullname))
                    onClear(self)
                    
            conn.commit()
            conn.close()
    else:
        messagebox.showerror("Missing Text Error!","Please enter correct data in all FIVE fields.")

#---------------
        
def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('stuTracker.db')
    with conn:
        cur = conn.cursor()
        # Check count to ensure that this is not the last record in
        #the dB ... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_stuTracker""") #count all rows
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation !","I got a match\nWanna burn a file?\n\
                                            \nAll info associated with \"{}\" will be permenantly deleted.\
                                            ".format(var_select))
            if confirm:
                conn = sqlite3.connect('stuTracker.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_stuTracker\
                                    WHERE col_fullname = '{}'""".format(var_select))
                    # Call the func to clear all of the textboxes and the selected index of listbox
                    onDeleted(self)
                    conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database \
                                            and cannot be deleted at this time".format(var_select))
    conn.close()

#---------------
    
def onDeleted(self): # Note this is onDeleted past-tense
    # Clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_curCourse.delete(0,END)
    try: # Deletes the username from the listbox (once it is deleted from dB)
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

#---------------
    
def onClear(self):
    # Clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_curCourse.delete(0,END)

#---------------
    
def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('stuTracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_stuTracker""")
        count = cursor.fetchone()[0]
        i=0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_stuTracker""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i += 1
    conn.close()

#---------------
    
def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # Index of the list selection
        var_value = self.lstList1.get(var_select) # List selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    
    # For name changes, the user will need to delete the entire record and start over.
     
    var_email = self.txt_email.get().strip() # Normalize the data to maintain dB integrity
    var_curCourse = self.txt_curCourse.get().strip()
    
    #Phone number with + for country code - needed for validation
    norm_phone = self.txt_phone.get().strip()
    countryCode= '+'
    var_phone = countryCode + norm_phone
    
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_curCourse)>0): # Ensure that there is data present

        #validating the phone number
        parsePhoneNo = phonenumbers.parse(var_phone)
        isPhoneNoValid= phonenumbers.is_valid_number(parsePhoneNo)

        # Error message if the phone is not valid
        if isPhoneNoValid == False: 
            messagebox.showerror("Invalid Phone Number!","Please enter a valid phone number!\n (country code)(area code)(phone number)")

            print(isPhoneNoValid)

        #verify email layout
        elif not "@" or not "." in var_email:  
            messagebox.showerror("Invalid Email!","Please enter a valid email!")

        else:    
            conn = sqlite3.connect('stuTracker.db')
            with conn:
                cur = conn.cursor()

                # Count records to see if the user's changes are already in
                #the dB...meaning, there are no changes to update.
                cur.execute("""SELECT COUNT(col_phone) FROM tbl_stuTracker \
                            WHERE col_phone = '{}'""".format(var_phone))
                
                #count for the phone
                count = cur.fetchone()[0] 
                #!!!Dev purpose only!!!
                print (count) 
                
                cur.execute("""SELECT COUNT(col_email) FROM tbl_stuTracker \
                            WHERE col_email = '{}'""".format(var_email))
                
                count2 = cur.fetchone()[0] #count for the email
                print(count2) #!!!Dev purpose only!!!

                cur.execute("""SELECT COUNT(col_curCourse) FROM tbl_stuTracker \
                            WHERE col_curCourse = '{}'""".format(var_curCourse))
                
                count3 = cur.fetchone()[0] #count for the curCourse
                print(count3) #!!!Dev purpose only!!!
                
                if count == 0 or count2 == 0 or count3 == 0: # If proposed changes are not already in the database, then proceed
                    response = messagebox.askokcancel("Update Request","The following changes ({}), ({}) and ({}) will be implemented \
                                                        for ({}).\n\nProceed with the update request?\
                                                        ".format(var_phone,var_email,var_curCourse,var_value))
                    print(response) #!!!Dev purpose only!!!
                    if response:
                        with conn:
                            cursor = conn.cursor()
                            cursor.execute("""UPDATE tbl_stuTracker SET \
                                            col_phone = '{0}',col_email = '{1}',col_curCourse = '{2}\
                                            WHERE col_fullname = '{3}'"""\
                                            .format(var_phone,var_email,var_curCourse,var_value))
                            onClear(self)
                            conn.commit()
                    else:
                        messagebox.showinfo("Cancel request","No changes have been made to ({})".format(var_value))
                else:
                    messagebox.showinfo("No changes detected","({}), ({}) and ({}) \nalready exist in the database \
                                        for this name.\n\nYour update has been cancelled\
                                        ".format(var_phone,var_email,var_curCourse))
                onClear(self)
            conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list.\nThen edit \
                                the phone or email or current_course information.")
    onClear(self)
                                                                                                                                 
#===================================================================================
# Program flow control Section:
#==============================

if __name__ == "__main__":
    pass

#===================================================================================
#===================================================================================
