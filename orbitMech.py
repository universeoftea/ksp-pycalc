import math

class Orbit:


    def __init__(self,ap,pe,pbody):
        """ Note that ap, pe is altitude above surface level of parent body
            pbody is an object of type CelestialBody"""


        self.parentBody = pbody
        self.apoapsis = self.parentBody.radius + ap
        self.periapsis = self.parentBody.radius + pe
        self.gravitation = 6.67 * 10 ** (-11)
        self.semiMajorAxis = (self.apoapsis + self.periapsis) / 2
        if self.periapsis == self.apoapsis:
            self.circular = True
        else:
            self.circular = False

    def getVel(self,altitude):
        """ Gets the velocity for a certain altitude in the orbit
        altitude is in m above surface"""

        #TODO: Check pe<alt<ap
        #TODO: Implement getVelCirc into this function
        radi = altitude + self.parentBody.radius
        v = math.sqrt(self.gravitation * self.parentBody.mass * (2 / radi - 1 / self.semiMajorAxis))
        return v

    def getVelCirc(self):
        if self.circular:
            v = math.sqrt(self.gravitation * self.parentBody.mass * (1 / self.semiMajorAxis))
            return v
        else:
            return "Orbit is not circular"

class Hoffman:

    def __init__(self,origin,target,pbody):

        self.origin = Orbit(origin,origin,pbody)
        self.target = Orbit(target,target,pbody)
        self.transfer = Orbit(target,origin,pbody)

    def h1deltaV(self):
        deltaV = self.transfer.getVel(self.transfer.periapsis) - self.origin.getVelCirc()
        return deltaV

    def h2deltaV(self):
        deltaV = self.target.getVelCirc() - self.transfer.getVel(self.transfer.apoapsis)
        return deltaV

    def deltaVtotal(self):
        deltaV = self.h1deltaV() + self.h2deltaV()
        return deltaV

    #TODO: Time in transfer orbit (h1 to h2)
    #TODO: Target burn angle, (needs to implement angle position in Orbit class
