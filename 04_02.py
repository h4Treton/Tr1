class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return 'Цвет: {0}, Кол. мест: {1}, есть дет.кресло: {2}, занята: {3}'.format(self.color,
                                                                                     self.count_passenger_seats,
                                                                                     'да' if self.is_baby_seat else 'нет',
                                                                                     'да' if self.is_busy else 'нет')


class Taxi:
    def __init__(self, cars):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for el in self.cars:
            if el.count_passenger_seats == count_passengers and el.is_baby_seat == is_baby and not el.is_busy:
                el.is_busy = True
                return el
        return None


car1 = Car('красный', 5, True)
car2 = Car('синий', 2, False)
car3 = Car('зеленый', 4, True)
taxi1 = Taxi([car1, car2, car3])
print(taxi1.find_car(5, True))
print(taxi1.find_car(5, True))
print(taxi1.find_car(3, True))
print(taxi1.find_car(2, False))
