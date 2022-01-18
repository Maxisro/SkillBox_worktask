# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return 'Всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail=tail
#         )
#
#     def walk(self):
#         print('Гуляет')
#
#
# class Cat(Pet):
#     def sound(self):
#         print('Мяу')
#
#
# class Dog(Pet):
#     def sound(self):
#         print('Гав!')
#
#
# class Frog(Pet):
#     has_tail = False
#
#     def sound(self):
#         print('Ква!')
#
#     def walk(self):
#         print('Плавает')
#
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(frog)
# frog.sound()
# print(cat)
# print(dog)
# cat.sound()
# dog.sound()
# cat.walk()


class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)

    def get_count(self):
        return self.__count

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Студент учится в университете {}'.format(self.university)
            )
        )
        return info
        # return 'Студент {} учится в университете {}'.format(self.get_name(), self.university)


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Компания: {}\tЗарплата: {}'.format(self.company, self.salary)
            )
        )
        return info


my_student = Student(name='Tom', age=24, university='MSU')
print(my_student)

my_emp = Employee(name='Bob', age=25, salary=1000, company='Google')
print(my_emp)