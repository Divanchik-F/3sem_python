class Mother:
    def name(self):
        return "Mother"

    def __str__(self):
        return self.name()


class Daughter(Mother):
    def name(self):
        return "Daughter"


mth=Mother()
dt=Daughter()
print(mth)
print(dt)
