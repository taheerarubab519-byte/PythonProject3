class Elevator:
    def __init__(self, bottom, top):
        self.current_floor = bottom
        self.bottom = bottom
        self.top = top

    def go_to_floor(self, floor):
        self.current_floor = floor
        print(f"Elevator is now on floor {self.current_floor}")

class Building:
    def __init__(self, bottom, top, elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = []
        for _ in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number - 1].go_to_floor(destination)

    def fire_alarm(self):
        print("Fire alarm! ")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"\nElevator {i}:")
            elevator.go_to_floor(self.bottom_floor)

b = Building(1, 10, 2)
b.run_elevator(1, 5)
b.run_elevator(2, 8)
b.fire_alarm()