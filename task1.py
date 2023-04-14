# Задача №1
# #реализовать дескрипторы для любых двух классов


class ProtectSign:

    def __set__(self, param, value):
        if not isinstance(value, str) or not value.isalpha:
            raise ValueError("Эти значения только буквенные")
        param.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    # def __set_name__(self, owner, my_attr):
    # #     # owner - владелец атрибута - <class '__main__.Worker'>
    # #     # my_attr - имя атрибута владельца - hours, rate
    #     self.my_attr = my_attr
class Defence_age:
    
    def __set__(self, var, value):
        if value < 18:
            raise ValueError("Возраст работающего на вредном производстве может быть менее 18 лет")
        var.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class ProtectSalary:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, var, value):
        if value < 12000:
            raise ValueError("Зарплата не может быть ниже прожиточного минимума 12000 рублей")
        var.__dict__[self.my_attr] = value


class Worker:
    
    name = ProtectSign() # имя атрибута, который делаем дескриптором, в конструктор не передаем
    surname = ProtectSign() # имя атрибута, который делаем дескриптором, в конструктор не передаем
    age = Defence_age() # имя атрибута, который делаем дескриптором, в конструктор не передаем
    position = ProtectSign() # имя атрибута, который делаем дескриптором, в конструктор не передаем
    income = ProtectSalary("income") # выполнено с передачей параметра атрибута (для примера)

    def __init__(self, name, surname, position, age, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.age = age
        self.income = wage + bonus

class Position(Worker):

    def get_full_name(self):

        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income

#     def string(self):
#         return self.get_full_name() + " " + self.position \
# + " доход " + str(self.get_total_income())


w1 = Position("Петр", "Петров", "полотер", 25, 44000, 3000)
print(end="\n")
print(f"{w1.surname} {w1.name}, {w1.position}, возраст {w1.age} лет, \
доход с бонусом {w1.get_total_income()} рублей ")
#print(w1.string())
print(end="\n")

