# The Black_Hole class is derived from Simulton; it updates by finding+removing
#   any class derived from Prey whose center is contained inside its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import math



class Black_Hole(Simulton):  
    radius = 10
    def __init__(self, x, y):

        self.width_height = 2 * self.radius
        Simulton.__init__(self, x,y, self.width_height, self.width_height)


    def update(self, m):
        def to_eat(simulton):
            if isinstance(simulton, Prey) and self.contains(simulton.get_location()):
                return True
        preys = m.find(to_eat)
        for i in preys:
            m.remove(i)

        return preys

    def display(self, the_canvas):
        the_canvas.create_oval(self._x - self.get_dimension()[0]/2, self._y - self.get_dimension()[1]/2, self._x + self.get_dimension()[0]/2,
                                  self._y + self.get_dimension()[1]/2, fill='black')


    def contains(self,xy):

        return self.distance(xy) <= self.get_dimension()[0]/2

