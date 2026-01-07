class Elevator:
    def __init__(self, bottom, top):
        self.floor = bottom

    def floor_up(self):
        self.floor += 1
        print("Floor:", self.floor)

    def floor_down(self):
        self.floor -= 1
        print("Floor:", self.floor)

    def go_to_floor(self, choice):
        while self.floor < choice:
            self.floor_up()
        while self.floor > choice:
            self.floor_down()

h1 = Elevator(1, 10)
print("Go to the fifth floor:")
h1.go_to_floor(5)
print("\nCome back to the bottom floor:")
h1.go_to_floor(1)