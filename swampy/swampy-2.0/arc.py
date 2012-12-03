from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def arc(bob , r, angle):
 
    import math 
    arc_length = 2 * math.pi * r * angle /360
    n = int (arc_length /3) + 1
    step_length = arc_length/3
    step_angle = float(angle)/ n

    for i in range (n):
    	fd(bob, step_length)
        lt(bob,step_angle) 
                

arc(bob,13,270)

import pdb
pdb.run('w')

wait_for_user()

	

