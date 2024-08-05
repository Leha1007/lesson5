class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: {} , количество этажей {}'.format(self.name, self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        return House(self.name, self.number_of_floors)

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
        elif isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
        return House(self.name, self.number_of_floors)

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors *= other
        elif isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
        return House(self.name, self.number_of_floors)

    def __truediv__(self, other):
        if isinstance(other, int):
            if other != 0:
                self.number_of_floors /= other
            else:
                return 'на ноль делить нельзя'
        elif isinstance(other, House):
            if other.number_of_floors != 0:
                self.number_of_floors /= other.number_of_floors
            else:
                return 'на ноль делить нельзя'
        return House(self.name, self.number_of_floors)

    __radd__ = __add__
    __iadd__ = __add__


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__