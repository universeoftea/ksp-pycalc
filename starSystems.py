import orbitMech

class CelestialBody:
    """ Easy implementation of a celestial body, orbit of the body does not have to be defined
    Orbit is only implemented for future use, planetary transfers etc """

    def __init__(self,bodyName,bodyRadius,bodyMass,orbit=None):
        self.name = bodyName
        self.radius = bodyRadius
        self.mass = bodyMass
        self.orbit = orbit
