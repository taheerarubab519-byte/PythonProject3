class Elevator:
    def __init__(self, bottom, top):
        self.current_floor = bottom
        self.bottom = bottom
        self.top = top

    def go_to_floor(self, floor):
        self.current_floor = floor
        print(f"Elevator on floor {self.current_floor}")

class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        self.elevators[elevator_number - 1].go_to_floor(destination)

b = Building(1, 10, 2)

b.run_elevator(1, 7)
b.run_elevator(2, 8)