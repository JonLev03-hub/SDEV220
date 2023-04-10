class Vehicle():
    def __init__(self, t):
        self.type = t


class Automobile(Vehicle):
    def __init__(self, year, make, model, numDoors, roofType):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.number_of_doors = numDoors
        self.type_of_roof = roofType


# create the car object with user input
params = [
    input("Please enter the Vehicle year: "),
    input("Please enter the Vehicle make: "),
    input("Please enter the Vehicle model: "),
    input("Please enter the Vehicle door count: "),
    input("Please enter the Vehicle sunroof type: "),

]
car = Automobile(*params)

for key, value in car.__dict__.items():
    print(f"{key}: {value}")
