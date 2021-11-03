# "х" - количество этажей в доме (от одного и более); "y" - этаж, на котором находится лифт.
class Elevator:
    def __init__(self, x=5, y=3):
        self.x = x
        self.y = y

    # Поднять лифт.
    def up(self):
        if self.y < self.x:
            self.y += 1
            print(f'Лифт поднимается на {self.y} этаж')
        else:
            print('Лифт не может подняться выше')

    ## Опустить лифт.
    def down(self):
        if self.y > 1:
            self.y -= 1
            print(f'Лифт опускается на {self.y} этаж')
        else:
            print('Лифт не может опуститься ниже')
