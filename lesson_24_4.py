# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             'Name: {} \nSalary: {}'.format(self.name, self.salary)
#         )
#
#
# emp_1 = Employee('Tom', 10000)
# emp_2 = Employee('Bob', 20000)
#
# emp_1.print_info()
# emp_2.print_info()


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')

        else:
            print('Вся картошка созрела. Можно собирать!\n')


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()