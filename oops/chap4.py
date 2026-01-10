class Vehicle:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting..")

class Car(Vehicle):
    def __init__(self,brand,model, doors):
        super().__init__(brand,model)
        self.doors = doors

my_car = Car("Ford","Focus",4)
my_car.start()
print(f"It has {my_car.doors} doors")
