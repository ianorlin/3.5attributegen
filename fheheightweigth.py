#!/usr/bin/env python3

#Copyright 2015

import random 

modifier= random.randint(1,8)+random.randint(1,8)


hieght=60+modifier

wieght= 90+ 5* modifier

print ("Height= ", hieght//12, " feet ", hieght%12 , "inches")

print ("Weight= ", wieght, "pounds.")

