from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

#class Polygon():
def polygon(t,l,n):
       	angle = 360.0/n
	for i in range (n):
       		fd(bob, l)
       		lt(bob,angle) 
                

polygon(bob,10,50)




wait_for_user()

	

