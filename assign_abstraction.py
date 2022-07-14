#===================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:   ABSTRACTION SUBMISSION ASSIGNMENT
"""
                Create a class that utilizes the concept of abstraction.
                    Your class should contain at least one abstract method and one regular method.  
                Create a child class that defines the implementation of its parents abstract method.
                Create an object that utilizes both the parent and child methods.
"""

#===================================================================================
#================
# Import Section:
#================
# abc 'Abstract Base Class'
from abc import ABC, abstractmethod

#=============
#Main Section:
#=============

# Class that utilizes the concept of abstraction.
class Robots (ABC):

    # Regular method of this class
    def paySlip (self, amount):
        print("Your purchase amount: ",amount)

    # Abstract method with requirement of passing one argument
    @abstractmethod
    def payment(self,amount):
        pass


# Child class that defines the implementation of its parents abstract method.   
class debitCardPayment(Robots):

    # defining how to implement the payment function from it's parent class
    def payment(self,amount):
        print('Your purchase amount of {} will de deducted from your account.'.format(amount))


# Objects that utilizes both the parent and child methods.
# Instantiating of obj 
obj = debitCardPayment()

# Passing in arguments for inherited method and abstract method
obj.paySlip('$1000')
obj.payment('$1000')


#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first

if __name__ == "__main__":
    #start() #name of function
    pass    #pass if no function is called internally
    
#===================================================================================
#===================================================================================
