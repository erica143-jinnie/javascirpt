class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileague = mileage
    class bus (Vehicle):
        pass
    school_bus = bus("School Volvo",180,12)
    print("Vehicle name:", School_bus.name,"speed:",
    School_bus.max_speed,"mileage:",School_bus.mileage)