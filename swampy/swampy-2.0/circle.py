from TurtleWorld import *
from Polygon import *


world = TurtleWorld()
t = Turtle()

def circle(t,r):

        import math
	circumfrence = 2 * math.pi * r
        n = 50
        l = circumfrence / n
        polygon(t,l,n)     
                
circle(t,15)




wait_for_user()

	

