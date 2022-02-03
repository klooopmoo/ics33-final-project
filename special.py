from PIL.ImageTk import PhotoImage
from PIL import Image
from prey import Prey


#special introduces another prey. Upon death the prey becomes 2 other prey with double speed stats.

class Special(Prey):
    Radius = 10
    def __init__(self, x, y, respawn = 1, gif ='ezgif-6-186c3c2ea67c.gif', speed = 6 ):

        self.respawn = respawn
        self.gif = gif
        Prey.__init__(self, x, y,2* self.Radius, 2* self.Radius, 0, speed)
        self._image = PhotoImage(Image.open(gif).resize((60,60), Image.ANTIALIAS))
        self.randomize_angle()


    def update(self, m):
        self.move()


    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image = self._image)

    def remove(self, m):
        gif = 'BouncyWelcomeGrassspider-max-1mb.gif'


        if self.respawn > 0:
            self.respawn -=1
            self.move()
            self.randomize_angle()
            self.move()
            self.move()
            special1 = Special(*self.get_location(),self.respawn, gif, 12)
            special2 = Special(*self.get_location(), self.respawn, gif, 12 )


            m.add(special1)
            m.add(special2)
            special2.move()
            special1.move()
