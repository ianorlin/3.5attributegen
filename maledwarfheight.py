#!/usr/bin/env python3

#Copyright 2016 Brendan Perrine
# This is free software released under the GPL v3

import random

random.seed()

# dd5 modifier
modifier= random.randint(1,4)+ random.randint(1,4)
# in inches converting base hieght to only inches
height = 45 + modifier

#7x weight modifier
weight = 150+ 7*modifier

print("height= ", height//12, "feet", height % 12 ,"inches")


print ("weight= ", weight ,"pounds")
