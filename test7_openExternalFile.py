#
# Python:   3.10.5
#
# Author:   Mirwais Sarwary
#
# Purpose:  The Tech Academy - Python Course.
#           Demonstrating how to link (read and print)to external file.
#===================================================================================

###IMPORT SECTION###
import os #operating system

###Functions###
def openFile():
    '''
        Opens and reads files
    '''
    with open ('Data_for_python_tests.txt','r') as f:
        data = f.read()
        print(data)
        f.close() #avoid memory leaks

def writeData():
    '''
        Opens and writes on the files (append new data)
    '''
    #data to append
    data = '\nThis is new appended data!'
    #with open== do code only when file is open
    with open ('Data_for_python_tests.txt','a') as f:
        f.write(data)
        f.close() #avoid memory leaks

#Controlling the flow of programs
if __name__=="__main__":
    writeData()
    openFile()
