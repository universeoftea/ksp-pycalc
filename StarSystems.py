import orbitMech

class CelestialBody:

    def __init__(self,bodyName,bodyRadius,bodyMass,orbit):
        self.name = bodyName
        self.radius = bodyRadius
        self.mass = bodyMass
        self.orbit = orbit

class Kerbol:
    Kerbol = CelestialBody('Kerbol',261600000,1.7565459*10**28,None)

    Moho = CelestialBody('Moho',250000,2.5263314*10**21,orbitMech.Orbit(6315765981,4210510628,Kerbol))

    Eve = CelestialBody('Eve',700000,1.2243980*10**23,orbitMech.Orbit(9931011387,9734357701,Kerbol))
    Gilly = CelestialBody('Gilly',13000,1.2420363*10**17,orbitMech.Orbit(48825000,14175000,Eve))
    
    Kerbin = CelestialBody('Kerbin',600000,5.2915158*10**22,orbitMech.Orbit(13599840256,13599840256,Kerbol))
    Mun = CelestialBody('Mun',200000,9.7599066*10**20,orbitMech.Orbit(12000000,12000000,Kerbin))
    Minmus = CelestialBody('Minmus',60000,2.6457580*10**19,orbitMech.Orbit(47000000,47000000,Kerbin))
    
    Duna = CelestialBody('Duna',320000,4.515427*10**21,orbitMech.Orbit(21783189163,19669121365,Kerbol))
    Ike = CelestialBody('Ike',130000,2.7821615*10**20,orbitMech.Orbit(3296000,3104000,Duna))

