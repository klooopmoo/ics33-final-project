# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    DEATH_CLOCK = 30
    def __init__(self, x, y):

        self.death_clock = Pulsator.DEATH_CLOCK

        Black_Hole.__init__(self, x,y)

    def update(self, m):
        number_simultons = len(super().update(m))
        if number_simultons > 0:
            self.death_clock = Pulsator.DEATH_CLOCK

            self.change_dimension(number_simultons, number_simultons)



        else:
            self.death_clock -= 1
            if self.death_clock == 0:

                self.change_dimension(-1, -1)


                if self.get_dimension()[0] == 0:
                    m.remove(self)
                else:
                    self.death_clock = Pulsator.DEATH_CLOCK




