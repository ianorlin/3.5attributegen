#!/usr/bin/env python3

#copyright 2015 Brendan Perrine

#This will implement the pathrfinreder whiehgt weight for male humans from pathfinder rpg. 

import random

random.seed()
#2d10 modifier
modifier= random.randint(1,10)+random.randint(1,10)

wieght= 120+ 5*modifier

print ("wieght= " , wieght, " Pounds")

height=58+modifier

print( "height= ", height//12 , "feet", height %12 , " inches.")
