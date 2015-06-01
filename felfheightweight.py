#! /usr/bin/env python3

# Copyright 2015 Brendan Perrine

import random

random.seed()

# modifier 2d6 
modifier= random.randint(1,6)+random.randint(1,6)

#base ehight female elf in inches
height=64+modifier

weight= 90+ modifier*3 


print("height= ", height//12 , "feet, ", height%12 , "inches.")

print (" weight= ", weight, "pounds.")
