# Задача №2
# Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

class SimpleMeta(type):
    first = None

    def __call__(self):
        if self.first == None:
            self.first = super().__call__()
        return self.first


class MyClass(metaclass=SimpleMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()
obj_5 = MyClass()

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_4)
print(obj_4 is obj_5)
print(obj_5 is obj_1)