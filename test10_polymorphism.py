#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Date:         7/5/22
#
# Assignment:   Polymorphism Submission assignment
#===================================================================================
#----------------------------------------------------------
#imports:
#none

#-----------------------------------------------------------
#Main Code:

#parent class
class Robot:
    #Attributes of the class
    def __init__(self,speciality,controls,active):
        self.speciality = speciality
        self.controls = controls
        self.active = active

    #methods of the class
    def information(self):
        msg = "\nSpeciality: {}\nControls: {}\nActive: {}\n".format(self.speciality,self.controls,self.active)
        return msg

#Child class instance
class Medic(Robot): #(Robot)==inheriting parent
    #Attributes inherited and new ones
    def __init__(self,name,speciality,controls,active):
        # super()inherits parent attributes
        super().__init__(speciality,controls,active)
        self.name = name
        self.legs = 'Dual_lower_extremities'
        self.arms = 'Quad_upper_extremities'
        
    #methods
    def information(self):
        msg = "\nName: {}\nUpper Extremities: {}\nLower Extremities: {}\nSpeciality: {}\nControls: {}\nActive:{}".format(self.name,self.arms,self.legs,self.speciality,self.controls,self.active)
        return msg
    
    def Prime_Objective(self):
        msg = "\n {}\'s primary objective: \n'To save lives by all means necessary'".format(self.name) 
        return msg

class Combat(Robot): #(Robot)==inheriting parent
    #Attributes inherited and new ones
    def __init__(self,name,speciality,controls,active):
        # super()inherits parent attributes
        super().__init__(speciality,controls,active)
        self.name = name
        self.legs = 'AT_wheels'
        self.arms = 'Dual_upper_extremities'
        
    #methods
    def information(self):
        msg = "\nName: {}\nUpper Extremities: {}\nLower Extremities: {}\nSpeciality: {}\nControls: {}\nActive: {} \n".format(self.name,self.arms,self.legs,self.speciality,self.controls,self.active)
        return msg
    
    def Prime_Objective (self):
        msg = "\n {}\'s primary objective: \n'To protect and neutralize hostile forces'".format(self.name)
        return msg

    

#-----------------------------------------------------------
#program flow control
if __name__ == "__main__": #looks at this first to see which script to run first
    #Instanciating and printing info
    Robot =Robot('Robotics Design and Service','State of the art',True)
    print (Robot.information())
    
    Med_Robo1 = Medic('Meddie','Medic Service','Autonomous',True)
    print (Med_Robo1.information())
    print (Med_Robo1.Prime_Objective())

    Blood_Robo1 = Combat('Boomer','combat Service','VR controlled',True)
    print (Blood_Robo1.information())
    print (Blood_Robo1.Prime_Objective())
    
