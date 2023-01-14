#!/usr/bin/python3

class Vehicles:

    def __init__(self):
        pass
       #print('Vehicles is a ', vehicleType)

                         

                         # Defining Child class

class Car(Vehicles):
    def __init__(self):

        Vehicles.__init__(self)

                                                  

                                                  # Driver's code  

print(issubclass(Car, Vehicles))

print(issubclass(Car, list))

print(issubclass(Car, Car))

print(issubclass(Car, (list, Vehicles)))
