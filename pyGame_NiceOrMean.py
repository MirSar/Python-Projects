#
# Python:   3.10.5
#
# Author:   Mirwais Sarwary
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember: function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable to
#           back to the calling function
#===================================================================================
#Title: Nice or Mean Game


#imports:
import cv2
import numpy as np


#Functions:
def start(nice=0, mean=0, name=""):#controlling with default values
    # get User's name
    name = describe_game(name) #calling a function
    nice,mean,name = nice_mean(nice,mean,name) #calling a function

def describe_game(name):
    '''
        check to see if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    '''
    # meaning, if we do not alrady have this user's name,
    # then they are a new player and we need to get thier name
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("\nbut at the end of the game your fate\nwill be sealed by your actions.")
                    stop = False
    return name #returning the user's name
    
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice or mean? (N/M)\n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you\nmenacingly and storms off...")
            mean = (mean+1)
            stop = False
    score(nice,mean,name)# pass the 3 variables to the score()

def show_score(nice,mean,name):
    print ("\n{}, your current total:\n({},Nice) and ({},Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    print("\nNice job {0}, you win!\n{0} Everyone loves you and you've \nmade lots of friends along the way!".format(name))

    #importing image using OpenCV
    window_name = "YouWin"
    img = cv2.imread("images/YouWin.png", cv2.IMREAD_COLOR)
    cv2.imshow(window_name, img)
    #make the popup window appear on top
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #Substitue the {} wildcards with our variable values
    print("\nAhhh too bad, game over!\n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))

   #importing image using OpenCV
    window_name = "YouLose"
    img = cv2.imread("images/YouLose.png", cv2.IMREAD_COLOR)
    cv2.imshow(window_name, img)
    #make the popup window appear on top
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #call again function and pass in our variables
    again(nice,mean,name)
    
def again(nice,mean,name):
    stop=True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset (nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes' or (N) for 'No':\n>>> ")
            
def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)
        

#program flow control
if __name__ == "__main__": #looks at this first to see which script to run first
    start()
