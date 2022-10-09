class Shape:
    def __init__(self,l,w):
        self.w=w
        self.l=l
    
    
class Triangle(Shape):
    def area(self):
        return (self.w*self.l/2)

class Rectangle(Shape):
    def area(self):
        return (self.w*self.l)



l=int(input())
w=int(input())
tr=Triangle(l,w)
rec=Rectangle(l,w)
print(tr.area())
print(rec.area())
