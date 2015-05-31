#! /usr/bin/env python3

#Copyright 2015 Brendan Perrine

import random

random.seed()

modifier= random.randint(1,4) + random.randint(1,4)

#converting base to inches
height= 43+modifier

weight=120 + 7*modifier

print ( "weight= ", weight ,"Pounds")

print (" height= ", height//12, " feet, " , height%12 ," inches")
