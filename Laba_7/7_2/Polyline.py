from Vec2d import Vec2d
import pygame

class Polyline:
    def __init__(self, _gameDisplay, _steps = 35):
        self.gameDisplay = _gameDisplay

        self.steps = _steps
        self.points = []
        self.speeds = []

    def add_point(self, _point, _speed):
        self.points.append(_point)
        self.speeds.append(_speed)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p]+self.speeds[p]
            if self.points[p].x>self.gameDisplay.get_width() or self.points[p].x<0:
                self.speeds[p]=Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y>self.gameDisplay.get_height() or self.points[p].y<0:
                self.speeds[p]=Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            knot = Knot(self.gameDisplay).get_knot(self.points, self.steps)
            for p_n in range(-1, len(knot) - 1):
                pygame.draw.line(self.gameDisplay, color, knot[p_n].int_pair(), knot[p_n+1].int_pair(), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(self.gameDisplay, color, p.int_pair(), width)


class Knot(Polyline):
    def get_knot(self, _points, _steps):
        self.points = _points
        self.steps = _steps
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            self.ptn = []
            self.ptn.append((self.points[i]+self.points[i+1])*0.5)
            self.ptn.append(self.points[i+1])
            self.ptn.append((self.points[i+1]+self.points[i+2])*0.5)

            res.extend(self.get_points())
        return res

    def get_points(self):
        alpha = 1/self.steps
        res = []
        for i in range(self.steps):
            res.append(self.get_point(i*alpha))
        return res

    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.ptn) - 1
        if deg == 0:
            return self.ptn[0]
        return self.ptn[deg]*alpha+self.get_point(alpha, deg-1)*(1-alpha)