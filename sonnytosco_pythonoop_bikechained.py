class Bike(object):
    def __init__(self, price,max_speed):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
        print "Created a new bike"
    def displayInfo(self):
        print "Bike's price:"+ str(self.price)
        print "Bike's max speed:"+str(self.max_speed)+'mph'
        print "Bike's mileage:"+str(self.miles)+'miles'
        return self
    def ride(self):
        print 'Riding'
        self.miles+=10
        return self
    def reverse(self):
        print 'Reversing'
        if self.miles>=5:
            self.miles-=5
        return self
bike1 = Bike(99.99, 12)
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(139.99, 20)
bike2.ride().ride().reverse().reverse().displayInfo()


# Answer:
# class Bike(object):
#     def __init__(self, price, max_speed):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = 0
#
#     def displayInfo(self):
#         print 'Price is: $' + str(self.price)
#         print 'Max speed: ' + str(self.max_speed) + 'mph'
#         print 'Total miles: ' + str(self.miles) + ' miles'
#
#     def drive(self):
#         print 'Driving'
#         self.miles += 10
#
#     def reverse(self):
#         print 'Reversing'
#         # prevent negative miles
#         if self.miles >= 5:
#             self.miles -= 5
#
# # create instances and run methods
# bike1 = Bike(99.99, 12)
# bike1.drive()
# bike1.drive()
# bike1.drive()
# bike1.reverse()
# bike1.displayInfo()
#
# bike2 = Bike(139.99, 20)
# bike2.drive()
# bike2.drive()
# bike2.reverse()
# bike2.reverse()
# bik2.displayInfo()
