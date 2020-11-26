class Stationery:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw

    def metod(self):
        print('Draw metod: ')

class Pen(Stationery):
    def metod(self):
        print('Pen draw')

class Pencil(Stationery):
    def metod(self):
        print('Pencil draw')

class Handle(Stationery):
    def metod(self):
        print('Handle draw')

pen = Pen('pen', 'line')
pencil = Pencil('penscil', 'thin line')
handle = Handle('handle', 'draw')

pen.metod()
pencil.metod()
handle.metod()
