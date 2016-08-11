Inheritance
When you form a new class using classes that have already been defined. It allows
one class to take on some or even all of its attributes and methods from a parent class.
Benefits of inheritance are code reuse and reduction of complexity of a program.
Derived classes can override or extend the functionality of base classes.

Using the human object:
import random                    # import the random module
class Human(object):
  def __init__(self, clan=None):
    print 'New Human!!!'
    self.health = 100
    self.clan = clan
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3
  def taunt(self):
    print "You want a piece of me?"
  def attack(self):
    self.taunt()
                                 # use the random module to generate a number when we attack
    luck = round(random.random() * 100)
    if(luck > 50):
      if(luck * self.stealth > 150):
        print 'attacking!'
        return True
      else:
        print 'attack failed'
        return False
    else:
      self.health -= self.strength
      print "attack failed"
      return False

Say we want to create child classes called Wizard, Ninja, and Samurai. They all
inherit the blueprint of class Human, but they add their own blueprint.
To create new classes in a file called new_classes.py:
from human import Human
class Wizard(Human):
  def heal(self):
    self.health += 10
class Ninja(Human):
  def steal(self):
    self.stealth += 5
class Samurai(Human):
  def sacrifice(self):
    self.health -= 5
# create new instance of Wizard, Ninja, and Samurai
harry = Wizard()
rain = Ninja()
tom = Samurai()
# all instances still have human properties because its
# class inherits from the Human class
print harry.health
print rain.health
print tom.health
# yet they are subclasses which mean they can extend the current functionality of Human class
# instances of the Wizard class can perform the heal method
harry.heal()
print harry.health
# instances of the Ninja class can perform the steal method
rain.steal()
print rain.stealth
# instances of the Samurai class can perform the sacrifice method
tom.sacrifice()
print tom.health
print tom.stealth

The general skeleton for implicit inheritance is as follows:
class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes
