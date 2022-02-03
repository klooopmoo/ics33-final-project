# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    DISTANCE_CONSTANT = 200
    def __init__(self, x, y):
        self.distance_constant = Hunter.DISTANCE_CONSTANT
        #Pulsator
        Pulsator.__init__(self, x,y)
        #Mobile_simulton
        Mobile_Simulton.__init__(self, x,y, 2 * self.radius, 2 * self.radius, 0, 5)
        self.randomize_angle()


    def update(self, m):
        Pulsator.update(self,m)
        def to_eat(simulton):
            return isinstance(simulton, Prey) and self.distance(simulton.get_location()) <= 200

        hunter_eat = m.find(to_eat)

        if len(hunter_eat) != 0:
            prey_list = {}
            for prey in hunter_eat:
                distance_ = self.distance(prey.get_location())
                prey_list[prey] = distance_

            prey_name = min(prey_list, key=lambda x: prey_list[x])

            prey_location = prey_name.get_location()
            hunter_location = self.get_location()
            self.set_angle(atan2(prey_location[1] - hunter_location[1], prey_location[0] - hunter_location[0]))

        self.move()
