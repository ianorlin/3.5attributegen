#!/usr/bin/env python3

#Copyright 2015 Brendan Perrine. 
#this file is liscensed under the gpl v3 and does the pathfinder algorythm for female random height and weight. 


import random

random.seed()


modifier= random.randint(1,10)+random.randint(1,10)

weight= 85+5*modifier
#female height in inches.
height=53 +modifier

print( "weight= ", weight, "Pounds")

# ok to get hieght in feet and inches need to 

hfeet= height//12
hinches=height%12

print ("height= ", hfeet, "feet" , hinches, "inches")


