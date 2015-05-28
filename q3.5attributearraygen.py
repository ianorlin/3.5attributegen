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
from PyQt5.QtWidgets import *
import random
import sys
final_attributes=[]
intermediate_attributes=[]
random.seed()

 

for attribute in range(1,7): 
    temp_rolls=[]
    for dice in range (1,5):
       #roll 4d6 and drop the lowest.
       temp_rolls+= [random.randint(1,6)]
    temp_rolls=sorted(temp_rolls)
    intermediate_attributes+= [sum(temp_rolls[1:4])]
    #if (attribute == 6):
       # print (sorted(final_attributes, reverse=True))

# sort the stats not in order but with reverse of normal from high to low
intermediate_attributes= sorted (intermediate_attributes, reverse=True)
for stat in range(0,6):
    final_attributes+= str(intermediate_attributes[stat]) +','

# Make Qt5 GUI frontend

class Window(QWidget):
    def __init__(self):
       super(Window, self).__init__()
       layout=QGridLayout()
       self.setLayout(layout)

       label=QLabel("your character stats are:")

       layout.addWidget(label,0,0)
       label=QLabel(''.join(final_attributes))
       layout.addWidget(label,1,0) 
      #need to get to  a string to print the join method of string is what we want here.  
      # label= QLabel(sorted(final_attributes, reverse=True))
      # layout.addWidget(label,0,2)

app= QApplication(sys.argv)   

screen=Window()
screen.show()


sys.exit(app.exec_())
