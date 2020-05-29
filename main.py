import orbitMech
import starSystems



def openStarSystemData(star_system_datafile_name):
    
    star_system = []
    
    star_system_datafile = open(star_system_datafile_name, "r")
    index = 0
    for line in star_system_datafile:
        if "Name: " in line:
            index = index + 1
            body_name = line.replace("Name: ","")
            body_name = body_name.replace("\n","")
            print("Initializing celestial body: " + body_name)
        elif "Radius:" in line:
            body_radius = float(line.replace("Radius:",""))
            print("Radius: " + str(body_radius))
        elif "Mass:" in line:
            body_mass = float(line.replace("Mass:",""))
            print("Mass: " + str(body_mass))
        elif ";" in line:
            print("Finished reading data for " + body_name + "\n")
            star_system.append( starSystems.CelestialBody(body_name,body_radius,body_mass) )
    
    star_system_datafile.close()

    return star_system




datafile_name = 'kerbol.txt'
star_system = openStarSystemData(datafile_name)
print(star_system[0].name)
