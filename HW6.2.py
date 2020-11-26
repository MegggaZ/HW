class Road:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def all_road(self):
        x = self.l * self.w * 25 * 5
        return x


road = Road(20, 5000)
print(road.all_road())
