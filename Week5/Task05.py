class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometers = 0

    def drive(self, hours, speed):
        actual_speed = min(speed, self.max_speed)
        self.kilometers += actual_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasolineCar("ACD-123", 165, 32.3)

e_car.drive(3, 180)
g_car.drive(3, 160)

print("Kilometers of Electric car are:", e_car.kilometers)
print("Kilometers of Gasoline car are:", g_car.kilometers)