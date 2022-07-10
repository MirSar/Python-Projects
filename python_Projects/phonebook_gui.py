#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Assignment:   phonebook application
#               phonebook_gui file contains all of the code
#               for our graphical user widgets         
#
# Date:         7/7/2022
#
#===================================================================================
#----------------------------------------------------------
# Import Section:

from tkinter import *
import tkinter as tk

# Importing our other custome modules
import phonebook_main
import phonebook_func

#-----------------------------------------------------------
# Main Section:

# Defining functions

def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry
        (pack vs grid: grid offers the best control for
        pacing the widgets)
    """
    #creating instances of widgets - labels
    self.lbl_fname = tk.Label(self.master,bg='green',fg='yellow',text = 'First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_lname = tk.Label(self.master,bg='green',fg='yellow', text = 'Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_phone = tk.Label(self.master,bg='green',fg='yellow', text = 'Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_email = tk.Label(self.master,bg='green',fg='yellow', text = 'Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_user = tk.Label(self.master,bg='green',fg='yellow', text = 'Contact List:')
    self.lbl_user.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    #creating the widgets - text Entry
    self.txt_fname = tk.Entry(self.master,bg='lightblue',text = '')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_lname = tk.Entry(self.master,bg='lightblue',text = '')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master,bg='ghostwhite',text = '')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_email = tk.Entry(self.master,bg='ghostwhite',text = '')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,bg='aliceblue',exportselection=0,yscrollcommand=self.scrollbar1.set)
    #'binding' to our listbox an event-listener (user clicks or selects)
    self.lstList1.bind('<<ListboxSelect>>',lambda event:phonebook_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    #creating buttons
    self.btn_add = tk.Button(self.master,width=12,height=2,bg='lightgreen',fg='darkblue',text='Add',command=lambda:phonebook_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    
    self.btn_update = tk.Button(self.master,width=12,height=2,bg='lightgreen',fg='darkblue',text='Update',command=lambda:phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)

    self.btn_delete = tk.Button(self.master,width=12,height=2,bg='lightgreen',fg='darkblue',text='Delete',command=lambda:phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,bg='lightgreen',fg='darkblue',text='Close',command=lambda:phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    #calling functions
    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)
    

#-----------------------------------------------------------
# Program flow control Section:
        
if __name__ == "__main__":
    pass 
