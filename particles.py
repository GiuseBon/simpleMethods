import math

class particle():
    def __init__(self,x_coord,y_coord,M) -> None:
        self.x = x_coord
        self.y = y_coord
        self.mass = M

p1 = particle(1,2,5)
p2 = particle(-1,-3,7)
#calculate Total Mass of system
M = p1.mass + p2.mass
#calculate Center of mass
x_cm = p1.mass*p1.y + p2.mass*p2.y
x_cm = x_cm/M
y_cm = p1.mass*p2.x + p2.mass*p2.x
y_cm = y_cm/M

print(x_cm,y_cm)
