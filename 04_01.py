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


car1 = Car('красный', 5, True)
print(car1)
