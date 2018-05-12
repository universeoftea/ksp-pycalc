import math

class Orbit:


    def __init__(self,ap,pe,pbody):
        """ Note that ap, pe is altitude above surface level of parent body
            pbody is an object of type CelestialBody"""


        self.parentBody = pbody
        self.apoapsis = ap
        self.periapsis = pe
        self.gravitation = 6.67 * 10 ** (-11)
        self.semiMajorAxis = (self.apoapsis + self.periapsis) / 2
        if self.periapsis == self.apoapsis:
            self.circular = True
        else:
            self.circular = False

    def getVel(self,altitude=None):
        """ Gets the velocity for a certain altitude in the orbit
        altitude is in m from parent body CoM"""
        if altitude == None:
            altitude = self.periapsis

        return math.sqrt(self.gravitation * self.parentBody.mass * (2 / altitude - 1 / self.semiMajorAxis))


class Hoffman:

    def __init__(self,origin,target,pbody):

        self.origin = Orbit(origin,origin,pbody)
        self.target = Orbit(target,target,pbody)
        self.transfer = Orbit(target,origin,pbody)

    def h1deltaV(self):
        return self.transfer.getVel(self.transfer.periapsis) - self.origin.getVelCirc()
        
    def h2deltaV(self):
        return self.target.getVelCirc() - self.transfer.getVel(self.transfer.apoapsis)
        
    def deltaVtotal(self):
        return self.h1deltaV() + self.h2deltaV()
        
    #TODO: Time in transfer orbit (h1 to h2)
    def hDeltaT(self):
        return math.pi * math.sqrt( self.transfer.semiMajorAxis ** 3 / (self.transfer.gravitation * self.transfer.parentBody.mass) )
    #TODO: Target burn angle, (needs to implement angle position in Orbit class
