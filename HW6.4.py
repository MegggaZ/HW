class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{}'.format(self.name), 'is going')

    def stop(self):
        print('{}'.format(self.name), 'is stop')

    def turn(self, direction):
        print('{} is turn {}'.format(self.name, direction))

    def show_speed(self):
        print('Speed: ', self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Very quickly!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Very quickly!')


class PoliceCar(Car):
        pass

t_car = TownCar(80, 'green', 'BMW', False)
s_car = SportCar(150, 'red', 'Alfa Romeo', False)
w_car = WorkCar(50,'blue', 'ZIL', False)
p_car = PoliceCar(30, 'white', 'VAZ 2106', True)

t_car.show_speed()
s_car.stop()
w_car.turn('right')
p_car.go()

