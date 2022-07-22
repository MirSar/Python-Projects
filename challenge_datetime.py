#===================================================================================
#===================================================================================

# Python:       3.10.5

# Author:       Mirwais Sarwary

# Purpose:      The Tech Academy - Python Course

# Assignment:   Datetime CHALLENGE
"""
The Portland-based company you work for just opened two new branches.
One is in New York City, the other in London.
They need a very simple program to find out if the branches are open or closed.
The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.
"""

#===================================================================================
#================
# Import Section:
#================

from datetime import datetime
import pytz

#=============
#Main Section:
#=============

# current time
tz_time = datetime.now()

# current times in the Portland HQ, NYC branch, and London branch
# Portland using tz for Vancouver
portland_tz = pytz.timezone('America/Vancouver')
portland_time = tz_time.astimezone(portland_tz)
portland_time_only = portland_time.strftime("%X")

# london
london_tz = pytz.timezone('Europe/London')
london_time = tz_time.astimezone(london_tz)
london_time_only = london_time.strftime("%X")

# New York
newYork_tz = pytz.timezone('America/New_York')
newYork_time = tz_time.astimezone(newYork_tz)
newYork_time_only = newYork_time.strftime("%X")

# compare the time with each branch's hours to see if they are open or closed.
# Print out to the screen the three branches and whether they are open or closed.
if portland_time_only >= '09:00' and portland_time_only <= '15:00':
    print("The current time in Portland is "+portland_time_only)
    print("Porland HQ is Open!")
else:
    print("The current time in Portland is "+portland_time_only)
    print("Porland HQ is Closed!")

print("\n")

if london_time_only >= '09:00' and london_time_only <= '15:00':
    print("The current time in London is "+london_time_only)
    print("London branch is Open!")
else:
    print("The current time in London is "+london_time_only)
    print("London branch is Closed!")

print("\n")

if newYork_time_only >= '09:00' and newYork_time_only <= '15:00':
    print("The current time in New York is "+newYork_time_only)
    print("New York branch is Open!")
else:
    print("The current time in New York is "+newYork_time_only)
    print("New York branch is Closed!")
        
#===================================================================================
#program flow control:
#=====================
#looks at this first to see which script, if any, to run first

if __name__ == "__main__":
    pass    #name of function or pass
    
#===================================================================================
#===================================================================================
