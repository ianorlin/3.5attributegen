#!/usr/bin/env python3

#Copyright 2015 Brendan Perrine

import random

modifier=random.randint(1,8)+random.randint(1,8)

heigth=62+modifier

weigth= 110+5*modifier

print( "Height= ", heigth//12, " feet, ", heigth % 12, "inches")

print ("Weight= ", weigth, " pounds.")


