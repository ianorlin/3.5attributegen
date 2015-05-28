#rolls dice for character creation in dnd 3.5 or pathfinder rpg. 
#copyright 2014 Brendan Perrine 

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
    final_attributes+= [sum(temp_rolls[1:4])]
    if (attribute == 6):
        print (sorted(final_attributes, reverse=True))
