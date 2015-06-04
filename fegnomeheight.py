#!/usr/bin/env python3

#copyright 2015 Brendan Perrine

import random

random.seed()

modifier=random.randint(1,4)+random.randint(1,4)

height= 34+modifier

weight=30+modifier

print ("Height=", height //12 ," feet ", height%12, " inches.")

print ("Weight= ", weight, "pounds.")
