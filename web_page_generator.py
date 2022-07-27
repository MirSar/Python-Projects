#===================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:   Web Page Generator
"""
    1 Creates a GUI that allows the user to input text and initiate the web page generation process.
    2 Generates a web page that sets the user’s input as the body text for the web page.
    3 Opens the generated web page in a new tab in the browser.
"""

#===================================================================================
# Import Section:
#================
import tkinter as tk
from tkinter import *

# Allows you to create web documents and display them in the browser
import webbrowser

#=============
#Main Section:
#=============

# Creating the base GUI
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        # GUI Setup
        # creating an instance attribute that contains and saves the value of master
        # and makes it available to every method in your class.
        self.master = master

        # Specifying the size of the GUI
        #self.master.geometry('{}x{}'.format(600,300))

        # GUI title and config
        self.master.title("Web Page Generator")
        self.master.config(bg = 'gold')

        # Creates variable string for data entry
        self.displayText = StringVar()
        
        # Creates label
        self.lblTextEntry = Label(self.master,text='Enter and submit custom text or just click the Default HTML page button',font=("Helvetics",9), fg='black',bg='gold')
        self.lblTextEntry.grid(row=1,column=1,columnspan=3,padx=(10,10),pady=(10,0),sticky='W')

        # Creates data entry box
        self.txtEntry = Entry(self.master,text=self.displayText,font=('Helvetics',13),width=60,fg='black',bg='white')
        self.txtEntry.grid(row=2,column=1,columnspan=3,padx=(10,10),pady=(5,10),sticky='W')
        
        # Creates buttons
        self.btn = Button(self.master,text="Default HTML page",width=20,height=2,command=self.defaultHTML)
        self.btn.grid(row=3,column=2,columnspan=2,padx=60,pady=10,sticky=W)

        self.Submit_btn = Button(self.master,text="Submit Custom Text",width=20,height=2,command=self.subCustText)
        self.Submit_btn.grid(row=3,column=2,columnspan=2,padx=10,pady=10,sticky=E)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        # Open file and allow for file writing
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>"+ htmlText +"</h1>\n</body>\n</html>"
        # Write inside the opened file
        htmlFile.write(htmlContent)
        # Close the file once we are done
        htmlFile.close()
        # Displaying (open file) in a web browser
        webbrowser.open_new_tab("index.html")

    def subCustText(self):
        # Gets user input to display on webpage
        htmlText = self.displayText.get()
        # Open file and allow for file writing
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>"+ htmlText +"</h1>\n</body>\n</html>"
        # Write inside the opened file
        htmlFile.write(htmlContent)
        # Close the file once we are done
        htmlFile.close()
        # Displaying (open file) in a web browser
        webbrowser.open_new_tab("index.html")
 
#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first

if __name__ == "__main__":
    #instantiating Tkinter class object and calling it root 
    root =tk.Tk()
    #passing it to app
    App = ParentWindow(root)
    #to keep it alive, and continuously run...run mainloop()
    root.mainloop()
    
#===================================================================================
#===================================================================================
