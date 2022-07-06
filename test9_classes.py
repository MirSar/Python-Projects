#
# Python:       3.10.5
#
# Author:       Mirwais Sarwary
#
# Purpose:      The Tech Academy - Python Course
#
# Assignment:   Working with classes and OOP
#===================================================================================
#----------------------------------------------------------
#imports:
#none

#-----------------------------------------------------------
#Main Code:

#parent class
class Organism:
    #Attributes of the class
    name = "Unknown"
    species = "Unknown"
    legs = None #None has no data type == blank
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    #methods of the class
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}\n".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#Child class instance
class Human(Organism): #inheriting parent Organism
    #Attributes inherited
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    #methods
    def ingenuity (self):
        msg = "\nCreates weapon of choice with any given surrounding items" 
        return msg

#another child class instance
class Dog(Organism):
    #Attributes
    name = 'Ronin'
    species = 'husky and GSD'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    #methods
    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down with force and accuracy!"
        return msg
    
#another child class instance
class Bacterium(Organism):
    #Attributes
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    #methods
    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"
        return msg


#-----------------------------------------------------------
#program flow control
if __name__ == "__main__": #looks at this first to see which script to run first
    #Instanciating and printing info
    human = Human()
    print (human.information())
    print (human.ingenuity())

    dog = Dog()
    print (dog.information())
    print (dog.bite())

    bacteria = Bacterium()
    print (bacteria.information())
    print (bacteria.replication())
    
