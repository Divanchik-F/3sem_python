class Animal:

    def __init__(self, name, year):
        self.name=name
        self.year=year

    def __str__(self):
        return self.string()


class Zebra(Animal):

    def __init__(self, name, year):
        super().__init__(name, year)

    def string(self):
        return f"name:{self.name}, year:{self.year}, type:zebra"


class Dolphin(Animal):

    def __init__(self, name, year):
        super().__init__(name, year)

    def string(self):
        return f"name:{self.name}, year:{self.year}, type:dolphin"


zebra=Zebra("zzzzzzzzzz", 12)
print(zebra)
dolphin=Dolphin("dodo", 2)
print(dolphin.string())
