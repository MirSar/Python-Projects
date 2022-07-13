#

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:
'''Create a class that uses encapsulation.
                Requirements include:
                This class should make use of a private attribute or function.
                This class should make use of a protected attribute or function.
                Create an object that makes use of protected and private.'''

#===================================================================================
#================
# Import Section:
#================

#none

#=============
#Main Section:
#=============

# Create a class that uses encapsulation.
 
class Protected:
    def __init__ (self,*args):
        # uses single underscore
        self._protectedVar = 19
        self.userVar = args[0]
        self.userVar2 = args[1]

# demostrating that protected vars can still be changed
obj = Protected('Umar',63)

print ('the original value is {}'.format(obj._protectedVar))
print ('the userVar value is {}'.format(obj.userVar))
print ('the userVar2 value is {}'.format(obj.userVar2))

obj._protectedVar = 114
print ('the changed value is {}'.format(obj._protectedVar))


class Private:
    def __init__(self):
        # uses double underscore
        self.__privateVar = 13

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private
        
# demostrating that private vars can't be changed the same way as protected vars
obj2 = Private()

# On level higher protection...
# below method results in this error --> AttributeError: 'Private' object has no attribute '__privateVar'
#       print('current value of privateVar is {}'.format(obj2.__privateVar))
#       or print (obj2.__privateVar)

# using provided methods to print the private data
obj2.getPrivate()

# using provided methods to change the private data
obj2.setPrivate(99)
obj2.getPrivate()


#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first


if __name__ == "__main__":
##    start() #name of function
    pass    #pass if no function is called internally
    
#===================================================================================
#===================================================================================
