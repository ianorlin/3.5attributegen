#!/usr/bin/env python3

#Copyright 2015 Brendan Perrine

import random

random.seed()

#2d8 elf modifier
modifier= random.randint(1,8)+random.randint(1,8)

#base elf hiehgt in inches
height=64+modifier

weight= 100+ 3* modifier

print ("Height= ", height//12, " feet ", height % 12 ,"inches")

print ("Weight= ", weight, " pounds.")
