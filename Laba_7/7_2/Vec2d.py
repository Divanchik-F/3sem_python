class Vec2d:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __sub__(self, sec_num):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x-sec_num.x, self.y-sec_num.y)

    def __add__(self, sec_num):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x+sec_num.x, self.y+sec_num.y)

    def __len__(self):
        """возвращает длину вектора"""
        return (self.x*self.x+self.y*self.y)

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x*k, self.y*k)

    def int_pair(self):
        return self.x, self.y