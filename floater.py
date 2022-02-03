# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        self._image = PhotoImage(file='ufo.gif')
        super().__init__(x, y, self._image.width(), self._image.height(), 0, 5)
        self.randomize_angle()



    def update(self, item):
        speed_rate = random()
        if speed_rate <= .3:
            randomized_between_5 = random() - .5
            change_speed = max(3, self.get_speed() + randomized_between_5)
            new_speed = min(7, change_speed)
            self.set_velocity(new_speed, self.get_angle() + randomized_between_5)
        self.move()

    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image = self._image)
