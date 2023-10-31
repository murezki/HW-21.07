class Wheels:
    def __init__(self, count, type_):
        self.count = count
        self.type_ = type_


class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower


class Doors:
    def __init__(self, count, material):
        self.count = count
        self.material = material


class Car(Wheels, Engine, Doors):
    def __init__(self, count_wheels, type_wheels, fuel_type, horsepower, count_doors, material):
        Wheels.__init__(self, count_wheels, type_wheels)
        Engine.__init__(self, fuel_type, horsepower)
        Doors.__init__(self, count_doors, material)

car = Car(4, 'all-season', 'gasoline', 250, 4, 'steel')
print(f"количество колес {car.count}")
print(f"тип колес {car.type_}")
print(f"тип топлива {car.fuel_type}")
print(f"лошадиные силы {car.horsepower}")
print(f"количество дверей {car.count}")
print(f"материал дверей {car.material}")