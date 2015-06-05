#!/usr/bin/env python3

#Copyright 2015 Brendan Perrine


import random

random.seed()

modifier=random.randint(1,4)+random.randint(1,4)

height=36+modifier

weight= 35+modifier

print( "Height= ", height //12 , "feet", height%12 , "inches.")

print ("Weight= ", weight, "pounds.")
