# Parent class: Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = 100  # fuel level %

    def drive(self, distance):
        """Simulate driving, fuel decreases with distance"""
        fuel_needed = distance * 0.2
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"{self.brand} {self.model} drove {distance}km. Fuel left: {self.fuel:.1f}%")
        else:
            print(f"{self.brand} {self.model} does not have enough fuel!")

    def refuel(self):
        """Refill fuel tank"""
        self.fuel = 100
        print(f"{self.brand} {self.model} refueled to 100%")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - Fuel: {self.fuel:.1f}%"


# Child class: ElectricCar (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_range):
        # Call parent constructor
        super().__init__(brand, model, year)
        self.battery_range = battery_range
        self.battery = 100  # battery %

    # Polymorphism: override drive method
    def drive(self, distance):
        battery_needed = distance * (100 / self.battery_range)
        if self.battery >= battery_needed:
            self.battery -= battery_needed
            print(f"{self.brand} {self.model} (EV) drove {distance}km. Battery left: {self.battery:.1f}%")
        else:
            print(f"{self.brand} {self.model} (EV) battery too low!")

    def recharge(self):
        """Recharge battery"""
        self.battery = 100
        print(f"{self.brand} {self.model} battery recharged to 100%")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} (EV) - Battery: {self.battery:.1f}%"
    

# Example Usage
car1 = Car("Toyota", "Corolla", 2020)
car2 = ElectricCar("Tesla", "Model 3", 2023, battery_range=400)

print(car1)
print(car2)

car1.drive(50)
car2.drive(120)

car1.refuel()
car2.recharge()
