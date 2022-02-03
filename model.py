import controller
import model   # See how update_all should pass on a reference to this module

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
stop_step = False
click_objects = None
cycle_counter = 0
simultons = set()



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, stop_step, click_objects, cycle_counter, simultons
    running = False
    stop_step = False
    click_objects = None
    cycle_counter = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global stop_step, running
    running = True
    stop_step = True



#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)
def select_object(kind):
    global click_objects
    click_objects = kind



#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if click_objects == None:
        pass
    elif click_objects == 'Remove':
        for i in find(lambda i: i.contains((x,y))):
            if i in simultons:
                simultons.remove(i)

    else:
        simultons.add(eval('{} ({},{})'.format(click_objects, str(x), str(y))))




#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)


# remove simulton s from the simulation
def remove(s):
    global simultons
    if s in simultons:
        remove_method = getattr(s, 'remove', None)
        if callable(remove_method):
            remove_method(model)
        simultons.remove(s)




    #find/return a set of simultons that each satisfy predicate p
def find(p):
    simultons_true = set()
    for i in simultons:
        if p(i):
            simultons_true.add(i)

    return simultons_true


#call update for each simulton in this simulation (pass model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global running, stop_step, cycle_counter
    if running is True:
        cycle_counter += 1
        for i in simultons.copy():
            i.update(model)
    if stop_step is True:
        running = False
        stop_step = False




#For animation: (1st) delete all simultons on the canvas; (2nd) call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; (3rd) update the label defined in the controller for progress
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    for i in simultons:
        i.display(controller.the_canvas)

    string_to_text = '{} cycles {} simultons'.format(str(cycle_counter), str(len(simultons)))
    controller.the_progress.config(text=string_to_text)
