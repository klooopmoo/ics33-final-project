# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey):
    radius = 5
    def __init__(self, x, y):
        width_height = 2 * self.radius
        super().__init__(x, y, width_height, width_height,  0, 5)
        self.randomize_angle()


    def update(self, item):
        self.move()


    def display(self, canvas_update):
        canvas_update.create_oval(self._x - self.radius, self._y - self.radius, self._x + self.radius,
                                  self._y + self.radius, fill='blue')

