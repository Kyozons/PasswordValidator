import numpy

class Container:
    def __init__(self):
        self.list = []

    def add(self, value):
        self.list.append(value)
        return self.list.sort()

    def remove(self, value):
        if value in self.list:
            self.list.remove(value)
            return True
        else:
            return False

    def median(self):
        median = float(len(self.list) / 2)
        if median % 2 != 0:
            return self.list[int(median - .5)]
        else:
            return self.list[int(median - 1)]


container = Container()

container.add(1)
container.add(2)
container.add(2)

print(container.list)
container.median()
