from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(l,string):
	for i in range(4):
        	fd(bob, l)
        	lt(bob)
                print string

square(50,'hello')




wait_for_user()

	

