#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Assignment:   Learning built-in module Tkinter
#===================================================================================
#----------------------------------------------------------
#imports:
import tkinter
from tkinter import * #using all of it's widgets

#-----------------------------------------------------------
#Main Code:

#Frame is the parent class within Tkinter
#initialize setting and set class=self and Frame=master
class ParentWindow(Frame):  
    def __init__ (self,master):
        Frame.__init__(self)

        #setting things up...
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg = 'green')#background color

        #how to create variables
        self.varFName = StringVar()
        self.varLName = StringVar()

        #painting the text box
        #creating labels....using grid geometry to style
        self.lblFName = Label(self.master, text='First Name: ',font=("Helvetics",16), fg='gold',bg='green')
        self.lblFName.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblLName = Label(self.master, text='Last Name: ',font=("Helvetics",16), fg='gold',bg='green')
        self.lblLName.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = Label(self.master, text='',font=("Helvetics",16), fg='gold',bg='green')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))


        #calling class Entry to create data entry boxes
        #using grid geometry (google:python tkinter grid manager)
        self.txtFName = Entry(self.master, text=self.varFName,font=("Helvetics",16), fg='black',bg='lightblue')
        self.txtFName.grid(row=0,column=1,padx=(10,0),pady=(30,0))

        self.txtLName = Entry(self.master, text=self.varLName,font=("Helvetics",16), fg='black',bg='lightblue')
        self.txtLName.grid(row=1,column=1,padx=(10,0),pady=(30,0))

        #creating buttons
        #note: command= requires methods to be created
        self.btnSubmit = Button(self.master, text ='Submit',width=10,height=2, fg='green',bg='lightyellow',command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0),sticky=NE)

        self.btnCancel = Button(self.master, text ='Cancel',width=10,height=2, fg='red',bg='lightyellow',command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(0,90),pady=(30,0),sticky=NE)

    #create methods
    def submit(self):
        #get values from text boxes
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}'.format(fn,ln))
        
    def cancel(self):
        #clear text boxes
        self.master.destroy()
          



#-----------------------------------------------------------
#program flow control
#looks at this first to see which script to run first

if __name__ == "__main__":
    #instantiating Tkinter class object and calling it root 
    root =Tk()
    #passing it to app
    App = ParentWindow(root)
    #to keep it alive, and continuously run...run mainloop()
    root.mainloop()
