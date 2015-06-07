#! /usr/bin/env python3

#Copyright 2015 Brendan Perrine

import random

modifier= random.randint(1,8) + random.randint(1,8)

height= 62 + modifier

weight= 110+5*modifier

print(" height= ", height//12 ," feet ", height%12," inches.")

print ( " wieght= ", weight, " pounds.")

  
