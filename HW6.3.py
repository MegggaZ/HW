class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

    def all_income(self):
        self.__income = {'wage': int, 'bonus': int}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_full_income(self):
        return self._income_wage + self._income_bonus

position = (Position('Anton', 'Katyshev', 'worker', {'wage':5000,'bonus': 1000}))
print(position.get_full_name())
print(position.get_full_income())
