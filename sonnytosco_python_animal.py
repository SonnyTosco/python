class Animal(object):
    def __init__(self, name, health):
        self.name=name
        self.health=100
        print "RawrXD!"
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print "Animal:"+str(self.name)
        print "Health:"+str(self.health)

animal1=Animal("Jeff", 100)
animal1.walk().walk().walk().run().run().displayHealth()


# import random                      # import the random module
# class Human(object):               # define a new Human class
#     def __init__(self, clan=None): # define a parameter with a default value, clan
#       print 'New Human!!!'
#       # define attributes
#       self.health = 100
#       self.clan = clan
#       self.strength = 3
#       self.intelligence = 3
#       self.stealth = 3
#     # define methods
#     def taunt(self):               # pass self into all methods to access attributes
#       print "You want a piece of me?"
#     def attack(self):
#       self.taunt()                 # use the random module to generate a number when we attack
#       luck = round(random.random() * 100)
#       if(luck > 50):
#         if(luck * self.stealth > 150):
#           print 'attacking!'
#           return True
#         else:
#           print 'attack failed'
#           return False
#       else:
#         self.health -= self.strength
#         print "attack failed"
#         return False
