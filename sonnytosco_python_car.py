class Car(object):
    def __init__(self, price,speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        print "Created a new car"
    def displayInfo(self):
        print "Bike's price:"+ str(self.price)
        print "Bike's max speed:"+str(self.max_speed)+'mph'
        print "Bike's mileage:"+str(self.miles)+'miles'
    def ride(self):
        print 'Riding'
        self.miles+=10
    def reverse(self):
        print 'Reversing'
        if self.miles>=5:
            self.miles-=5
