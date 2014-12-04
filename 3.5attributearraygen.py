#!/usr/bin/env python3

import random
final_attributes=[]
random.seed()
for attribute in range(1,7): 
    temp_rolls=[]
    for dice in range (1,5):
       #roll 4d6 and drop the lowest.
       temp_rolls+= [random.randint(1,6)]
    temp_rolls=sorted(temp_rolls)
    final_attributes+= [temp_rolls[1:4]]
    if (attribute == 6):
        print (final_attributes)
#save to value


