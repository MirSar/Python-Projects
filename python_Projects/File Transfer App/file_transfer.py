#===================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:   File Transfer CHALLENGE
"""
Your employer wants a program developed to move files from one folder
to another with the click of a button.

Complete these actions:
    1.  Create a GUI: This GUI will act as the interface for users
        to transfer files from one directory to another. 
    2.  Automate: any files in the Customer Source directory that are new
        (or that were modified within the previous 24 hours)
        must be transferred into the Customer Destination folder.

"""

#===================================================================================
#================
# Import Section:
#================
import tkinter as tk
from tkinter import *

# to add func that allow user to select directories for the files
import tkinter.filedialog

# to create a function and button that will transfer the files
import os
import shutil

# timedelta() function of datetime library used for calculating
# differences in dates and also can be used for date manipulations
from datetime import datetime, timedelta

import time

#=============
#Main Section:
#=============

# Setup the GUI window
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        # Set the title of GUI window
        self.master.title("File Transfer")

        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20,command=self.sourceDir)
        # Positions source btn in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0,padx=(20,10),pady=(30,0))

        # Creates entry for source directory selection
        self.source_dir = Entry (width = 75)
        # Position for entry in GUI using grid()
        self.source_dir.grid(row=0, column=1, columnspan=2,padx=(20,10),pady=(30,0))

        # Creats btn to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20,command=self.destDir)
        # Positions destination btn in GUI using tkinter grid()
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry (width = 75)
        # Position for entry in GUI using grid()
        self.destination_dir.grid(row=1, column=1, columnspan=2,padx=(20,10),pady=(15,10))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files",width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2,column=1,padx=(200,0),pady=(0,15))

        # Creates an Exit button
        self.exit_btn = Button(text="Peace Out!",width=20,command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2,column=2,padx=(10,40),pady=(0,15))




    # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content entered in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0,END)
        # The .insert() mehtod will insert the user selection to the source_dir Entry
        self.source_dir.insert(0,selectSourceDir)

    # Creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content entered in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0,END)
        # The .insert() mehtod will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0,selectDestDir)

    # Creates function to transfer files from one dir to another
    def transferFiles(self):
        # Gets source directory using .get() method
        source = self.source_dir.get()
        # Gets destination directory using .get() mehtod
        destination = self.destination_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)

        # using the datetime() function to get the current time.
        current_time = datetime.now()
            
        # Runs through each file in the source directory
        for i in source_files:
            # Creates a complete path for each file
            filepath = str(source+'/'+i)
            # checks for any new or edited files within the last 24 hours.
            # Use the os.path.getmtime() function to get the timestamp of the file from it’s filepath
            time_stamp = os.path.getmtime(filepath)
            mod_time = datetime.fromtimestamp(time_stamp)

            # Deduct the current time from the timestamp of the files in the folder
            sinceMod_time = (current_time - mod_time)
            
            # Checking if the result of that deduction is less than 24 hours
            # if so then moves each file from the source to the destination
            if sinceMod_time <= timedelta(hours = 24):
                shutil.move(filepath,destination)
                print(i+' was successfully transferred.')
            else:
                print(i+ " is too old to transfer ;)")
                print("It has been ", sinceMod_time, " since it was last modified/created")
                print('\n')
            
    # Creates function to exit program
    def exit_program(self):
        # root is the main GUI window, the Tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
        


        
#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
#===================================================================================
#===================================================================================
