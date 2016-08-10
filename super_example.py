Super
- used when you want to update versions of methods that are defined in the parent class
because in addition to your custom code ou want to specifically call the parent
implementation of that method as well (or instead).
- in these cases you would reference that parent object with the keyword 'super'.

Parent __init__
- say that we wanted each f our sub-classes (wizard, ninja, samurai) to still inherit
the attributes of the parent Human class but we have more developed attributes than
the average Human. We could do that like this:

from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5

We'll see that they have the same attributes as the typical Human (the parent class),
but they also have beefed up attributes depending on which subclass we instantiated. 
