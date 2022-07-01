#
# Python:   3.10.5
#
# Author:   Mirwais Sarwary
# Date  :   June 30, 2022
#
# Purpose:  The Tech Academy - Python Course.
#           Demonstrating: creating an absolute file path 
#           source:
#           https://docs.python.org/3/library/os.path.html
#===================================================================================

###IMPORT SECTION###
import os

##Global Variables##

fName = 'Hello.txt' #file name
#not we need to use double \\ (escape key)
fPath = 'C:\\Users\\mirwa\\OneDrive\\Documents\\2 GitHub\\Python-Projects\\'

#using os methods to join fName and fPath#
abPath = os.path.join(fPath,fName)
print (abPath)
