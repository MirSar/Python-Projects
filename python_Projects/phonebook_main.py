#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Assignment:   phonebook application
#               phonebook_main file contains all of the basic info
#               definition of classes, and is the main code to run the app
#
# Date:         7/7/2022
#
#===================================================================================
#----------------------------------------------------------
# Import Section:

from tkinter import *
import tkinter as tk

# Importing our other custome modules
import phonebook_gui
import phonebook_func

#-----------------------------------------------------------
# Main Section:

# Defining classes
# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    #Note:'self' is for this class, and 'master' is for the imported Frame module
    def __init__(self, master,*args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master frame configuration
        self.master = master #this is the ParentWindow Frame
        self.master.minsize(500,300) #(height_px, width_px)
        self.master.maxsize(500,300)

        #This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Mir's Tkinter Phonebook :)")
        self.master.configure(bg='green')

        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "x" on the Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #Load in the GUI widgets from a separate module,
        #keeping this code compartmentalized and clutter free.
        phonebook_gui.load_gui(self)





#-----------------------------------------------------------
# Program flow control Section:
        
if __name__ == "__main__":
    #syntax used to create a window from Tkinter
    root = tk.Tk()
    #syntax to pass the created window to our App. attaching root (tk window) to our App
    App = ParentWindow(root)
    #Loop to keep the window open on our screen
    root.mainloop()
