
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет транспорта: {self.__color}')

    def print_info(self):
        return (f'Модель: {self.__model}\n'
                f'Мощность: {self.__engine_power}\n'
                f'Цвет: {self.__color}\n'
                f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    # Текущие цвета COLOR_VARIANTS = ['blue', 'red', 'green', 'BLACK', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
print(vehicle1.print_info())

    # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pearl')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
print(vehicle1.print_info())
