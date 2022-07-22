#==================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      Phonebook application: using Tkinter GUI

# Assignment:   The Tech Academy - Python Course
#               The tkinter package (“Tk interface”) is the
#               standard Python interface to the Tcl/Tk GUI toolkit.

#               phonebook_main = Main module of this phonebook app.
               
#               Contains: all of the basic info, program flow, and 
#               definitions of classes.

# Date:         7/7/2022

#===================================================================================
# Import Section: 
#================

# Running python -m tkinter from the command line...version of Tcl/Tk
# version Tcl/Tk 8.6
from tkinter import * 
import tkinter as tk

# Importing custom modules
import phonebook_gui 
import phonebook_func

#===================================================================================
# Main Section:
#==============

# Frame is the Tkinter frame class that our own class (ParentWindow) will inherit from.
# A frame is a widget that displays as a simple rectangle. Typically, you
# use a frame to organize other widgets both visually and at the coding level.
class ParentWindow(Frame):
    
    # Note: 'self' is for this class,
    # and 'master' is for the inherited parent class
    def __init__(self, master,*args, **kwargs): #any number of arguments and keyword arguments
        Frame.__init__(self,master,*args,**kwargs)

        # Define our master frame configuration with a
        # design paramenter = fixed window size
        self.master = master # this is the ParentWindow frame
        self.master.minsize(500,300) # size of window (width_px, height_px)
        self.master.maxsize(500,300)

        # Calling our custom 'phonebook_func.CenterWindow' method to center our app
        # on the user's screen.
        phonebook_func.center_window(self,500,300) # arguments are w,h

        # Title heading and bg color setting
        self.master.title("Mir's Tkinter Phonebook :)")
        self.master.configure(bg='green')

        # 'protocol()' method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "x" on the Windows OS.
        # Using custom method 'ask_quit()'
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Loading in the GUI widgets from a separate module,
        # keeping this code compartmentalized and clutter free.
        phonebook_gui.load_gui(self)

#===================================================================================
# Program flow control Section:
#==============================
       
if __name__ == "__main__":
    
    # Syntax used to create a window from Tkinter
    root = tk.Tk()
    
    # Syntax to pass the created window to our App.
    App = ParentWindow(root) # attaching root (tk window) to our App
    
    # Loop to keep the window open on our screen
    root.mainloop()

#===================================================================================
#===================================================================================
